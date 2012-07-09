from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Social Auth
    #url(r'', include('social_auth.urls')),
    (r'^user/', include('userena.urls')),

    # WKND urls
    url(r'^all-places/$', 'wknd.views.all_places', name='all_places'),
    url(r'^events/(?P<place_slug>[\w-]+)/(?P<event_slug>[\w-]+)/$', 'wknd.views.event', name='event'),
    #url(r'^events/(?P<pk>\d+)/apply/$', 'wknd.views.apply_event', name='apply_event'),
    #url(r'^events/(?P<pk>\d+)/resign/$', 'wknd.views.resign_event', name='resign_event'),
    
    #url(r'^register/$', 'wknd.views.registration', name='registration'),
    #url(r'^login/$', 'wknd.views.login_view', name='login'),
    #url(r'^logout/$', 'wknd.views.logout_view', name='logout'),
    url(r'^$', 'wknd.views.home', name='home'),
    
    # Admin
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
