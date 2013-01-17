from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from annoying.functions import get_object_or_None
from datetime import datetime, timedelta
from pytils.translit import slugify


"""
Utilitary models
"""
class Venue(models.Model):
    """
    A club, a theater or any other place where an even can be held.
    """
    # Common textual info.
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,)
    slug = models.SlugField()
    link = models.URLField()

    # city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    coords_lat = models.DecimalField(max_digits=20, decimal_places=17, blank=True,)
    coords_lng = models.DecimalField(max_digits=20, decimal_places=17, blank=True,)

    # Place manager
    # manager = models.ForeignKey(Manager)

    # logo =
    # image =

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title

    @property
    def has_manager(self):
        """
        Checks if Place has a profiile assigned as Manager.
        """
        # Local import to prevent recursive import.
        from usrs.models import Profile
        profile = get_object_or_None(Profile, manager_of=self)
        return True if profile else False


class Genre(models.Model):
    """
    Well, a genre.
    """
    # Title of a genre. Unique.
    title = models.CharField(max_length=100, unique=True,)

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title


"""
Main models
"""
class Event(models.Model):
    """
    An venue model.
    """
    # Place where the venue is held.
    venue = models.ForeignKey(Venue)

    # Actual date and time the venue is held on.
    date_time = models.DateTimeField(verbose_name='Date when venue starts')

    # Just a common title and text info.
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True,)

    # genre = models.ForeignKey(Genre).

    # Could be a link to an official page.
    link = models.URLField(blank=True,)

    # Slug to use in url. For better indexing.
    slug = models.SlugField(max_length=250,
                            unique_for_date="date_time",
                            blank=True,)

    # image =

    # Official price set.
    entry_price = models.DecimalField(max_digits=10, decimal_places=2,)

    # Price taken by list.
    entry_price_by_list = models.DecimalField(max_digits=10, decimal_places=2,)

    # Date and time until users can apply to an venue list.
    # They should be able to resign at any time.
    date_time_until_can_apply = models.DateTimeField()

    # Maximum people to be on the list.
    application_limit = models.PositiveIntegerField(default=0,)

    # Users that have applied.
    applied_users = models.ManyToManyField(User, blank=True,)

    class Meta:
        ordering = ('date_time',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Overriding save to automatically generate slug.
        """
        self.slug = "%s-on-%s" % (slugify(self.title),
                                  self.date_time.strftime("%B-%d-%Y")
                                  .lower())
        models.Model.save(self, *args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('venue', (), {'place_slug': self.place.slug,
                              'venue_slug': self.slug,})

    @staticmethod
    def get_current():
        """
        Return only actual venues. Venue date should be greater than now.
        """
        return Event.objects.select_related().\
                     filter(date_time__gt=datetime.now())

    # How many places left on the list.
    def get_spare_places(self):
        return None

    @property
    def starts_today(self):
        return True if self.date_time.date() == \
            datetime.today().date() else False

    @property
    def starts_tomorrow(self):
        return True if self.date_time.date() == \
            datetime.today().date() + timedelta(1) else False

    def user_can_apply(self, user):
        """
        Check if user can apply anything on that date.
        """
        # Check if current user have applied for anything held on the same day.
        user_applied_per_day = self.get_current().filter(
            applied_users=user,
            date_time__year=self.date_time.year,
            date_time__month=self.date_time.month,
            date_time__day=self.date_time.day,).count()

        # Return 'True' if it is less or equal than default setting.
        if user_applied_per_day < settings.APPLICATION_PER_DAY_LIMIT:
            return True
        return False

    def user_can_apply_this(self, user):
        """
        Check if user can apply for this particular venue.
        """
        # Return 'True' if user can apply today and haven't applied this venue.
        if self.user_can_apply(user) and user not in self.applied_users.all():
            return True
        return False

    def apply_user(self, user):
        if self.user_can_apply:
            self.applied_users.add(user)

    def user_can_resign_this(self, user):
        """
        Check if user can resign this particular venue.
        """
        # Return 'True' if user has already applied.
        if user in self.applied_users.all():
            return True
        else:
            return False

    def resign_user(self, user):
        if self.user_can_resign_this:
            self.applied_users.remove(user)
