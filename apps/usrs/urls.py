from django.conf.urls.defaults import *
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse_lazy

from .views import (LoginView,
                    RegularProfileView, RegularProfileEditView,
                    ManagerProfileView,)


urlpatterns = patterns('',
    url(r'^register/$', 'usrs.views.register', name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout, {'template_name': 'logout.html',
                               'next_page': reverse_lazy('home')}, name='logout'),

    # Regular user urls.
    url(r'^me/$', RegularProfileView.as_view(), name='regular_profile'),
    url(r'^me/edit/$', RegularProfileEditView.as_view(), name='regular_profile_edit'),

    # Place manager urls.
    url(r'^manager/$', ManagerProfileView.as_view(), name='manager_profile'),
)


"""
    TODO: A lot.
    signup
    activation

    user email check ?
    user pass check ?
    user favourites edit

    manager profile
    manager add/edit events
"""



"""
    # Signup, signin and signout
    #url(r'^signup/$', userena_views.signup, name='signup'),
    #url(r'^signin/$', userena_views.signin, name='userena_signin'),
    #url(r'^signout/$', userena_views.signout, name='userena_signout'),

    # Signup
    url(r'^(?P<username>[\.\w]+)/signup/complete/$',
       userena_views.direct_to_user_template,
       {'template_name': 'userena/signup_complete.html',
        'extra_context': {'userena_activation_required': userena_settings.USERENA_ACTIVATION_REQUIRED,
                          'userena_activation_days': userena_settings.USERENA_ACTIVATION_DAYS}},
       name='userena_signup_complete'),

    # Activate
    url(r'^(?P<username>[\.\w]+)/activate/(?P<activation_key>\w+)/$',
       userena_views.activate,
       name='userena_activate'),

    # Change password
    url(r'^(?P<username>[\.\w]+)/password/$',
       userena_views.password_change,
       name='userena_password_change'),
    url(r'^(?P<username>[\.\w]+)/password/complete/$',
       userena_views.direct_to_user_template,
       {'template_name': 'userena/password_complete.html'},
       name='userena_password_change_complete'),

    # Edit profile
    # url(r'^(?P<username>[\.\w]+)/edit/$',
    #   userena_views.profile_edit,
    #   name='userena_profile_edit'),

"""