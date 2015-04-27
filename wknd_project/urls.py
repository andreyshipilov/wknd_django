from django.conf.urls import patterns, include, url
from django.contrib import admin

import wknd.views
import usrs.views, usrs.urls


admin.autodiscover()

urlpatterns = patterns('',
    # Social Auth
    #url(r'', include('social_auth.urls')),
    

    # WKND urls
    url(r'^$', wknd.views.home, name='home'),
    url(r'^venues/$', wknd.views.venues, name='venues'),
    url(r'^venues/(?P<venue_slug>[\w-]+)/$', wknd.views.venue, name='venue'),
    url(r'^events/(?P<venue_slug>[\w-]+)/(?P<event_slug>[\w-]+)/$', wknd.views.event, name='event'),
    #url(r'^venues/(?P<pk>\d+)/apply/$', 'wknd.views.apply_venue', name='apply_venue'),
    #url(r'^venues/(?P<pk>\d+)/resign/$', 'wknd.views.resign_venue', name='resign_venue'),
    #url(r'^map/$', wknd.views.map, name='map'),
    
    #url(r'^register/$', 'wknd.views.registration', name='registration'),
    #url(r'^login/$', 'wknd.views.login_view', name='login'),
    #url(r'^logout/$', 'wknd.views.logout_view', name='logout'),
    url(r'', include(usrs.urls)),
    
    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
