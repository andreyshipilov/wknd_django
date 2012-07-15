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
from django.views.generic.edit import UpdateView, FormView
from django.views.generic.detail import DetailView

from .decorators import regular_user_required, manager_user_required
from .forms import RegistrationForm, RegularProfileEditForm
from .models import Profile
from wknd.models import Event


class RegistrationView(FormView):
    """
    New user register view.
    """
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Redirect to profile if is authenticated.
        if request.user.is_authenticated():
            return HttpResponseRedirect(request.user.profile.get_absolute_url())
        return super(RegistrationView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        #data = form.cleaned_data
        #data.email =
        return HttpResponseRedirect(self.get_success_url())


class LoginView(FormView):
    """
    Class based login view.
    """
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Redirect to profile if is authenticated.
        if request.user.is_authenticated():
            return HttpResponseRedirect(request.user.profile.get_absolute_url())
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        self.request.session.set_expiry(60 * 60 * 24 * 30)
        return HttpResponseRedirect(self.request.user.profile.get_absolute_url())


class RegularProfileView(DetailView):
    """
    Regular user view.
    """
    template_name = 'regular/profile.html'
    model = Profile

    @method_decorator(login_required(redirect_field_name=None))
    @method_decorator(regular_user_required)
    def dispatch(self, request, *args, **kwargs):
        return super(RegularProfileView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(RegularProfileView, self).get_context_data(**kwargs)
        context['favourites'] = self.get_object().profile.favourite_places.all()
        context['future_events'] = self.get_object().profile.get_future_events()
        context['passed_events'] = self.get_object().profile.get_passed_events()
        return context


class RegularProfileEditView(UpdateView):
    """
    Regular user edit profile view.
    """
    form_class = RegularProfileEditForm
    template_name = 'regular/profile_edit.html'
    success_url = reverse_lazy('regular_profile_edit')

    @method_decorator(login_required(redirect_field_name=None))
    @method_decorator(regular_user_required)
    def dispatch(self, request, *args, **kwargs):
        return super(RegularProfileEditView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user).user

    def form_valid(self, form):
        data = form.cleaned_data
        user = self.get_object()
        user.email = data['email'].lower()
        if data['password']:
            user.set_password(data['password'])
        user.save()
        return HttpResponseRedirect(self.get_success_url())


class ManagerProfileView(DetailView):
    """
    Manager profile view.
    """
    template_name = 'manager/profile.html'
    model = Profile

    @method_decorator(login_required(redirect_field_name=None))
    @method_decorator(manager_user_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ManagerProfileView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(ManagerProfileView, self).get_context_data(**kwargs)
        # Events added
        return context
