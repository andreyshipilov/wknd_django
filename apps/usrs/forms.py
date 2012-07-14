from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .models import Profile
from .utils import get_profile_model


class RegularEditProfileForm(forms.ModelForm):
    """
    Regular user profile edit form.
    """
    # Make all fields required
    def __init__(self, *args, **kwargs):
        super(RegularEditProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].required = True

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email')