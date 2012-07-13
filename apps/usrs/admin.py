from django.contrib import admin
from django import forms

from annoying.functions import get_object_or_None

from .models import *

class ProfileAdminForm(forms.ModelForm):
    """
    Change the admin view to handle some Place/Manger relations.
    """

    class Meta:
        model = Profile

    def clean_manager_of(self):
        data = self.cleaned_data

        # Check if place manager has a place defined.
        if data.get('user_type', None) == 2 and not data.get('manager_of', None):
            raise forms.ValidationError('Manager must have a place selected.')

        # Check if place selected only for manager type.
        if data.get('manager_of', None) and not data.get('user_type', None) == 2:
            raise forms.ValidationError('Regular users cannot be place managers.')

        # Check if manager is not chosen assigned for a taken place.
        if data.get('user', None) and data.get('manager_of', None):
            if data.get('manager_of').has_manager and \
            (data.get('manager_of').profile.user != data.get('user', None)):
                raise forms.ValidationError('Chosen place already has a \
                      manager: %s.' % data.get('manager_of').profile.user)
        return data['manager_of']

class ProfileAdmin(admin.ModelAdmin):
    list_display =('user', 'user_type', 'is_manager', 'is_regular',)
    list_filter = ('user_type',)
    form = ProfileAdminForm
admin.site.register(Profile, ProfileAdmin)
