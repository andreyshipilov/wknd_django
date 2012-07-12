from django.contrib import admin
from django import forms

from .models import *

class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Profile

    def clean_manager_of(self):
        data = self.cleaned_data

        if data.get('user_type', None) == 2 and\
        not data.get('manager_of', None):
            raise forms.ValidationError('Manager must have a place selected.')

        #if data.get('manager_of', None) and Place
        return data['manager_of']

class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
admin.site.register(Profile, ProfileAdmin)