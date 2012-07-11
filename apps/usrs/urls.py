from django.conf.urls.defaults import *
from django.contrib.auth.views import logout
# from django.core.urlresolvers import reverse


urlpatterns = patterns('',
    url(r'^register/$', 'usrs.views.register', name='register'),
    url(r'^login/$', 'usrs.views.login', name='login'),
    url(r'^logout/$', logout, {'template_name': 'logout.html', 'next_page': '/'}, name='logout'),

    url(r'^me/$', 'usrs.views.regular_profile', name='regular_profile'),
    url(r'^manager/$', 'usrs.views.manager_profile', name='manager_profile'),
)


"""    #url(r'^login/$', 'django.contrib.auth.views.login',
    #    {'template_name': 'login.html'},
    #    name='login',),"""


"""
    TODO: A lot.
    signup
    activation

    login
    logout

    user profile edit
        email check
        pass check
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
    #url(r'^(?P<username>[\.\w]+)/edit/$',
    #   userena_views.profile_edit,
    #   name='userena_profile_edit'),

"""