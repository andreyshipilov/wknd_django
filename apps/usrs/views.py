from django.core.urlresolvers import reverse_lazy
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView

from .decorators import regular_user_required, manager_user_required
from .forms import RegularEditProfileForm
from .models import Profile
from wknd.models import Event

@csrf_protect
def register(request):
    pass


@csrf_protect
@never_cache
def login(request):
    # Prevent access to login.
    if request.user.is_authenticated():
        # Redirect to profile.
        return HttpResponseRedirect(request.user.profile.get_absolute_url())

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username, password = (form.cleaned_data['username'],
                                  form.cleaned_data['password'])
            user = auth.authenticate(username=username,
                                password=password)
            if user.is_active:
                # If active - login.
                auth.login(request, user)
                # Set cookie for 30 days.
                request.session.set_expiry(60 * 60 * 24 * 30)
                # Redirect to profile.
                return HttpResponseRedirect(user.profile.get_absolute_url())
            else:
                pass
                # TODO: Give link to resend activation.
    else:
        form = AuthenticationForm()

    extra_context = {
        'form': form,
    }

    return render(request, 'login.html', extra_context)


class RegularProfile(DetailView):
    """
    Regular user view.
    """
    template_name = 'regular/profile.html'
    model = Profile

    @method_decorator(login_required(redirect_field_name=None))
    @method_decorator(regular_user_required)
    def dispatch(self, *args, **kwargs):
        return super(RegularProfile, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(RegularProfile, self).get_context_data(**kwargs)
        context['favourites'] = self.get_object().profile.favourite_places.all()
        context['future_events'] = self.get_object().profile.get_future_events()
        context['passed_events'] = self.get_object().profile.get_passed_events()
        return context


class RegularEditProfile(UpdateView):
    """
    Regular user edit profile view.
    """
    form_class = RegularEditProfileForm
    template_name = 'regular/profile_edit.html'
    success_url = reverse_lazy('regular_profile_edit')

    @method_decorator(login_required(redirect_field_name=None))
    @method_decorator(regular_user_required)
    def dispatch(self, *args, **kwargs):
        return super(RegularEditProfile, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user).user


class ManagerProfile(DetailView):
    """
    Manager profile view.
    """
    template_name = 'manager/profile.html'
    model = Profile

    @method_decorator(login_required(redirect_field_name=None))
    @method_decorator(manager_user_required)
    def dispatch(self, *args, **kwargs):
        return super(ManagerProfile, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(ManagerProfile, self).get_context_data(**kwargs)
        # Events added
        return context
