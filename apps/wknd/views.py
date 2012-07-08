from django.contrib import auth
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import *


def home(request):
    context = {
        'events': Event.get_current()
    }
    return render(request, 'home.html', context)

def all_places(request):
    context = {
        'places': Place.objects.all()
    }
    return render(request, 'all_places.html', context)

def event(request, place_slug, event_slug):
    event = get_object_or_404(Event, slug=event_slug, place__slug=place_slug)

    user_can_apply, user_can_apply_this, user_can_resign_this = False, False, False

    # Instantly apply or resign
    if request.method == "POST" \
    and request.POST.get("apply_or_resign", "") == "apply_or_resign":
        if event.user_can_apply_this(request.user):
            event.apply_user(request.user)
        elif event.user_can_resign_this(request.user): 
            event.resign_user(request.user)
        return HttpResponseRedirect(event.get_absolute_url())

    if request.user.is_authenticated():
        user_can_apply = event.user_can_apply(request.user)
        user_can_apply_this = event.user_can_apply_this(request.user)
        user_can_resign_this = event.user_can_resign_this(request.user)

    context = {
        'event': event,
        'user_can_apply': user_can_apply,
        'user_can_apply_this': user_can_apply_this,
        'user_can_resign_this': user_can_resign_this,
    }
    return render(request, 'event.html', context)


def apply_resign_event(request, pk):
    event = get_object_or_404(Event.get_current(), pk=pk)

    
          

""" Registration/Login/Logout views
"""
def registration(request):
    "Registration view."

    # Redirect authenticated user to home by default.
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))

    if request.method == "POST":
        # Get data from POST
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')

        if len(username) and len(password):
            "Save new user"
            new_user = User.objects.create_user(username, email, password)
            new_user.is_active = False
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()

            auth_user = auth.authenticate(username=username, password=password)
            auth.login(request, auth_user)

            # Redirect to a success page.
            return HttpResponseRedirect(reverse('home'))
        else:
            "Show errors."
            context = {
                'registration_failed': True,
            }
            return render(request, 'registration.html', context)
    else:
        # Else render the default form
        context = {}
        return render(request, 'registration.html', context)


def login_view(request):
    "Login view - basic auth and social networks auth."

    # Redirect authenticated user to home by default.
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))

    if request.method == "POST":
        # Get data from POST
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        # Login the user or tell to get lost.
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)

            # Redirect to a success page.
            return HttpResponseRedirect(reverse('home'))
        else:
            # Show an error page
            context = {
                'login_failed': True,
            }
            return render(request, 'login.html', context)
    else:
        # Else render the default form
        context = {}
        return render(request, 'login.html', context)

def logout_view(request):
    "Logout user and redirect to home page."
    
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))
