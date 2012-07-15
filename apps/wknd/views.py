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
