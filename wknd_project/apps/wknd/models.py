from django.db import models
from django.contrib.auth.models import User
# from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.utils.text import slugify

from annoying.functions import get_object_or_None
from datetime import datetime, timedelta
from autoslug import AutoSlugField


"""
Utilitary models
"""


class City(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        ordering = ("title",)
        verbose_name_plural = "cities"

    def __unicode__(self):
        return self.title


class Venue(models.Model):
    """
    A club, a theater or any other place where an even can be held.
    """
    # Common textual info.
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = AutoSlugField(populate_from="title", unique=True, max_length=100)
    link = models.URLField()
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City)
    post_code = models.PositiveSmallIntegerField()
    coords_lat = models.DecimalField(max_digits=20, decimal_places=17,
        blank=True, null=True)
    coords_lng = models.DecimalField(max_digits=20, decimal_places=17,
        blank=True, null=True)

    # Place manager
    # manager = models.ForeignKey(Manager)

    # logo =
    # image =

    class Meta:
        ordering = ("title",)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return (
            "venue", (),
            {"venue_slug": self.slug}
        )

    @property
    def has_manager(self):
        """
        Checks if Place has a profiile assigned as Manager.
        """
        # Local import to prevent recursive import.
        from usrs.models import Profile

        profile = get_object_or_None(Profile, manager_of=self)
        return True if profile else False

    @property
    def canonical_title(self):
        if self.title.lower().startswith(("the ", "a ")):
            return self.title.split(" ", 1)[1]
        else:
            return self.title

    @property
    def canonical_title_first_letter(self):
        return self.canonical_title[0]


class Genre(models.Model):
    """
    Well, a genre.
    """
    # Title of a genre. Unique.
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("title",)

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
    date_time = models.DateTimeField(verbose_name="Date when venue starts")

    # Just a common title and text info.
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    #genre = models.ForeignKey(Genre)

    # Could be a link to an official page.
    link = models.URLField(blank=True, )

    # Slug to use in url. For better indexing.
    slug = AutoSlugField(max_length=200, populate_from="title",
        unique_with="date_time")

    # image =

    # Official price set.
    entry_price = models.DecimalField(max_digits=10, decimal_places=2)

    # Price taken by list.
    entry_price_by_list = models.DecimalField(max_digits=10, decimal_places=2)

    # Date and time until users can apply to an venue list.
    # They should be able to resign at any time.
    date_time_until_can_apply = models.DateTimeField()

    # Maximum people to be on the list.
    application_limit = models.PositiveIntegerField(default=0)

    # Users that have applied.
    applied_users = models.ManyToManyField(User, blank=True)

    class Meta:
        ordering = ("date_time",)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Overriding save to automatically generate slug.
        """
        title_slug = slugify(self.title)
        date_slug = self.date_time.strftime("%B-%d-%Y").lower() \
            .replace('-0', '-')
        self.slug = "{0}-{1}".format(title_slug, date_slug)
        models.Model.save(self, *args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return (
            "event", (),
            {"venue_slug": self.venue.slug, "event_slug": self.slug}
        )

    @staticmethod
    def get_current():
        """
        Return only actual venues. Venue date should be greater than now.
        """
        return Event.objects.filter(date_time__gt=datetime.now()) \
            .select_related()

    @staticmethod
    def get_past():
        """
        Return only actual venues. Venue date should be greater than now.
        """
        return Event.objects.filter(date_time__lte=datetime.now()) \
            .select_related()

    @staticmethod
    def get_main_event():
        """
        Return only the main, first event.
        """
        return Event.get_current().annotate(
            applied_users_count=models.Count("applied_users"))[0]

    @staticmethod
    def get_secondary_events():
        """
        Return secondary events, first three.
        """
        return Event.get_current().annotate(
            applied_users_count=models.Count("applied_users"))[1:4]

    @staticmethod
    def get_tertiary_events():
        """
        Return secondary events, first three.
        """
        return Event.get_current().annotate(
            applied_users_count=models.Count("applied_users"))[4:]

    # TODO: How many places left on the list.
    def get_spare_places(self):
        return None

    @property
    def starts_today(self):
        return True if self.date_time.date() == datetime.today().date() \
            else False

    @property
    def starts_tomorrow(self):
        return True if self.date_time.date() == datetime.today().date() + \
                                                timedelta(1) else False

    def user_can_apply(self, user):
        """
        Check if user can apply anything on that date.
        """
        # Check if current user have applied for anything held on the same day.
        user_applied_per_day = self.get_current().filter(
            applied_users=user,
            date_time__year=self.date_time.year,
            date_time__month=self.date_time.month,
            date_time__day=self.date_time.day).count()

        # Return "True" if it is less or equal than default setting.
        if user_applied_per_day < settings.APPLICATION_PER_DAY_LIMIT:
            return True
        return False

    def user_can_apply_this(self, user):
        """
        Check if user can apply for this particular venue.
        """
        # Return "True" if user can apply today and haven't applied this venue.
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
        # Return "True" if user has already applied.
        if user in self.applied_users.all():
            return True
        else:
            return False

    def resign_user(self, user):
        if self.user_can_resign_this:
            self.applied_users.remove(user)
