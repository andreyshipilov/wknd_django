from django.contrib import auth
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Venue, Event


def home(request):
    context = {
        'events': Event.get_current(),
        'is_home': True,
    }
    return render(request, 'home.html', context)


def all_events(request):
    context = {
        'places': Venue.objects.all()
    }
    return render(request, 'all_venues.html', context)


def event(request, venue_slug, event_slug):
    event = get_object_or_404(Event, slug=event_slug, venue__slug=venue_slug)

    user_can_apply, user_can_apply_this, user_can_resign_this = False, False, False

    # Instantly apply or resign
    if request.method == "POST" \
    and request.POST.get("apply_or_resign", "") == "apply_or_resign":
        if venue.user_can_apply_this(request.user):
            venue.apply_user(request.user)
        elif venue.user_can_resign_this(request.user): 
            venue.resign_user(request.user)
        return HttpResponseRedirect(venue.get_absolute_url())

    if request.user.is_authenticated():
        user_can_apply = venue.user_can_apply(request.user)
        user_can_apply_this = venue.user_can_apply_this(request.user)
        user_can_resign_this = venue.user_can_resign_this(request.user)

    context = {
        'venue': venue,
        'user_can_apply': user_can_apply,
        'user_can_apply_this': user_can_apply_this,
        'user_can_resign_this': user_can_resign_this,
    }
    return render(request, 'venue.html', context)
