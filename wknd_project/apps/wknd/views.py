from django.contrib import auth
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from meta.views import Meta


from .models import Venue, Event


def home(request):
    context = {
        'main_event': Event.get_main_event(),
        'secondary_events': Event.get_secondary_events(),
        'tertiary_events': list(Event.get_tertiary_events()),
        'is_home': True
    }
    return render(request, 'home.html', context)


def venues(request):
    context = {
        'venues': Venue.objects.all()
    }
    return render(request, 'venues.html', context)


def venue(request, venue_slug):
    venue = get_object_or_404(Venue, slug=venue_slug)
    upcoming_events = Event.get_current().filter(venue=venue)
    past_events = Event.get_past().filter(venue=venue)

    meta = Meta(
        title=venue.title,
        url=venue.get_absolute_url(),
        description=venue.description,
    )

    context = {
        'meta': meta,
        'venue': venue,
        'upcoming_events': upcoming_events,
        'past_events': past_events
    }
    return render(request, 'venue.html', context)


def event(request, venue_slug, event_slug):
    event = get_object_or_404(Event, slug=event_slug, venue__slug=venue_slug)
    user_can_apply = False
    user_can_apply_this = False
    user_can_resign_this = False

    meta = Meta(
        title=event.title,
        url=event.get_absolute_url(),
        description=event.description,
    )

    # Instantly apply or resign
    if request.method == 'POST' and request.POST.get('apply_or_resign',
            '') == 'apply_or_resign':
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
        'meta': meta,
        'event': event,
        'user_can_apply': user_can_apply,
        'user_can_apply_this': user_can_apply_this,
        'user_can_resign_this': user_can_resign_this,
    }
    return render(request, 'event.html', context)
