from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .models import Profile

# from .utils import get_profile_model
import settings


class RegistrationForm(forms.ModelForm):
    """
    Form for creating a new user.
    """
    username = forms.RegexField(regex=r'^[\.\w]+$', max_length=30, label=_("Username"),
                                error_messages={'invalid': _('Username must contain only letters, numbers, dots and underscores.')})
    email = forms.EmailField(label=_("Email"), max_length=75)
    password = forms.CharField(label=_("Password"), min_length=3,
                               widget=forms.PasswordInput(render_value=True))

    def __init__(self, *args, **kwargs):
        # Make all fields required
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].required = True
        self.fields['first_name'].required = True

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',  'email',)

    def clean_username(self):
        """
        Validate username. Should not exists and not in forbidden list.
        """
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            pass
        else:
            raise forms.ValidationError(_('This username is already not yours.'))

        if self.cleaned_data['username'].lower() in settings.FORBIDDEN_USERNAMES:
            raise forms.ValidationError(_('You should not really use that username.'))
        return self.cleaned_data['username']

    def clean_email(self):
        """
        Validate unique e-mail address.
        """
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email):
            raise forms.ValidationError(_('This email is already in use.'))
        return email

    def save(self):
        """
        Create a new user and account. Return the newly created user.
        """
        data = self.cleaned_data
        username, email, password = data['username'], data['email'].lower(), data['password']
        first_name, last_name = data['first_name'], data['last_name']
        #new_user = Profile.objects.create_user(username, email, password,
        #                                       first_name, last_name)
        return new_user


class RegularProfileEditForm(forms.ModelForm):
    """
    Regular user profile edit form.
    """
    password = forms.CharField(label=_("New password"), required=False,
                               min_length=3, widget=forms.PasswordInput())

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
