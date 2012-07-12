from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError

from annoying.fields import AutoOneToOneField
import datetime

from wknd.models import Place
import settings


class Profile(models.Model):
    """
    Base user Profile model.

    """
    user = AutoOneToOneField(User, primary_key=True,)
    activation_key = models.CharField(max_length=40, blank=True,)

    # User differentiation.
    user_type = models.PositiveIntegerField(choices=settings.USER_TYPES,
                                            default=1, db_index=True,)
    # Regular user fields.
    favourite_places = models.ManyToManyField(Place, blank=True,
                                                   related_name='favourites',)
    # Place manager fields.
    manager_of = models.OneToOneField(Place, blank=True, null=True,)

    def __unicode__(self):
        return 'Profile for %s' % self.user

    @models.permalink
    def get_absolute_url(self):
        if self.is_regular:
            return ('regular_profile',)
        if self.is_manager:
            return ('manager_profile',)

    @property
    def is_regular(self):
        return True if self.user_type == 1 else False

    @property
    def is_manager(self):
        return True if self.user_type == 2 else False

    @property
    def has_place(self):
        return True if self.manager_of else False

    def activation_key_expired(self):
        """
        Checks if activation key is expired.

        """
        expiration_days = datetime.timedelta(days=settings.ACTIVATION_DAYS)
        return self.activation_key == settings.ACTIVATED or \
               (self.user.date_joined + expiration_date <= datetime_now())
    activation_key_expired.boolean = True
