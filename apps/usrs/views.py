from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect

from .decorators import regular_user_required, manager_user_required


@csrf_protect
def register(request):
    pass


@csrf_protect
@never_cache
def login(request):
    # Prevent access to login
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username, password = (form.cleaned_data['username'],
                                  form.cleaned_data['password'])
            user = auth.authenticate(username=username,
                                password=password)
            if user.is_active:
                auth.login(request, user)
                request.session.set_expiry(60 * 60 * 24 * 30)

                # Where to now?
                redirect_to = redirect_signin_function(
                    request.REQUEST.get(redirect_field_name), user)
                return redirect(redirect_to)
            else:
                return redirect(reverse('userena_disabled',
                                        kwargs={'username': user.username}))
    else:
        form = AuthenticationForm()

    extra_context = {}
    extra_context.update({
        'form': form,
    })

    return render(request, 'login.html', extra_context)


@login_required
@regular_user_required
def regular_profile(request):
    user = request.user

    extra_context = {}

    return render(request, 'regular/profile.html', extra_context)


@login_required
@manager_user_required
def manager_profile(request):
    user = request.user

    extra_context = {}

    return render(request, 'manager/profile.html', extra_context)
