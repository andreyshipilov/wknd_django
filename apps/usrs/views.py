from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from .decorators import regular_user_required, manager_user_required


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


@login_required(redirect_field_name=None)
@regular_user_required
def regular_profile(request):
    user = request.user
    extra_context = {}

    return render(request, 'regular/profile.html', extra_context)


@login_required(redirect_field_name=None)
@manager_user_required
def manager_profile(request):
    user, place = request.user, user.profile.manager_of
    extra_context = {
        'place': place,
        'user': user,
        'profile': user.profile,
    }

    return render(request, 'manager/profile.html', extra_context)
