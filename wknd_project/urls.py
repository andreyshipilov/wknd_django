from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



admin.autodiscover()

urlpatterns = patterns('',
    # Social Auth
    #url(r'', include('social_auth.urls')),
    

    # WKND urls
    url(r'^$', 'wknd.views.home', name='home'),
#    url(r'^all-places/$', 'wknd.views.all_events', name='all_places'),
    url(r'^events/(?P<place_slug>[\w-]+)/(?P<event_slug>[\w-]+)/$', 'wknd.views.event', name='event'),
    #url(r'^venues/(?P<pk>\d+)/apply/$', 'wknd.views.apply_venue', name='apply_venue'),
    #url(r'^venues/(?P<pk>\d+)/resign/$', 'wknd.views.resign_venue', name='resign_venue'),
    
    #url(r'^register/$', 'wknd.views.registration', name='registration'),
    #url(r'^login/$', 'wknd.views.login_view', name='login'),
    #url(r'^logout/$', 'wknd.views.logout_view', name='logout'),
    url(r'', include('usrs.urls')),
    
    # Admin
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
