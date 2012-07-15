from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .models import Profile
from .utils import get_profile_model


class RegularProfileEditForm(forms.ModelForm):
    """
    Regular user profile edit form.
    """
    password = forms.CharField(label=_("New password"),
                               widget=forms.PasswordInput(render_value=False),
                               required=False, min_length=3)

    def __init__(self, *args, **kwargs):
        # Make all fields required
        super(RegularProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['email'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].required = True

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',  'email',)
