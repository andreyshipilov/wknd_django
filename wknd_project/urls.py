from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Social Auth
    #url(r'', include('social_auth.urls')),
    

    # WKND urls
    url(r'^$', 'wknd.views.home', name='home'),
    url(r'^all-places/$', 'wknd.views.all_places', name='all_places'),
    url(r'^venues/(?P<place_slug>[\w-]+)/(?P<venue_slug>[\w-]+)/$', 'wknd.views.venue', name='venue'),
    #url(r'^venues/(?P<pk>\d+)/apply/$', 'wknd.views.apply_venue', name='apply_venue'),
    #url(r'^venues/(?P<pk>\d+)/resign/$', 'wknd.views.resign_venue', name='resign_venue'),
    
    #url(r'^register/$', 'wknd.views.registration', name='registration'),
    #url(r'^login/$', 'wknd.views.login_view', name='login'),
    #url(r'^logout/$', 'wknd.views.logout_view', name='logout'),
    url(r'', include('usrs.urls')),
    
    # Admin
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    
)