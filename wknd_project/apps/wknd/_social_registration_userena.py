from socialregistration.signals import connect as profile_connect

PERMISSIONS = {
    'profile': ('view_profile', 'change_profile'),
    'user': ('change_user', 'delete_user')
}

def social_connect_callback(sender, user, profile, client, **kwargs):
    """
    Create a profile for this user after connecting

    """
    # Create a userena user.
    # TODO: You could make it prettier by setting a ``activation_key`` of ``ALREADY_ACTIVATED``
    # and looking at good values for the other fields of the model.
    userenaSignup = UserenaSignup.objects.get_or_create(user=user)

    # Create profile for user
    try:
        new_profile = Profile.objects.get(user=user)
    except:
        new_profile = Profile.objects.create(user=user)

    # Set some minimal permissions
    for perm in PERMISSIONS['profile']:
        assign(perm, new_profile.user, new_profile)

    for perm in PERMISSIONS['user']:
        assign(perm, new_profile.user, new_profile.user)

profile_connect.connect(social_connect_callback)






""""""""""""""""""""""""""""""""""""""""""

from socialregistration.signals import connect as profile_connect
from userena.managers import ASSIGNED_PERMISSIONS

@receiver(socialregistration_signals.connect, sender = FacebookProfile, dispatch_uid = 'facebook.connect')
def social_connect_callback(sender, user, profile, client, **kwargs):
    """
    Create a profile for this user after connecting

    """
    # Create a userena user.
    # TODO: You could make it prettier by setting a ``activation_key`` of ``ALREADY_ACTIVATED``
    # and looking at good values for the other fields of the model.
    userenaSignup = UserenaSignup.objects.get_or_create(user=user)

    # Create profile for user
    try:
        new_profile = Profile.objects.get(user=user)
    except:
        new_profile = Profile.objects.create(user=user)

    # Give permissions to view and change profile
    for perm in ASSIGNED_PERMISSIONS['profile']:
        assign(perm[0], user, new_profile)

    # Give permissions to view and change itself
    for perm in ASSIGNED_PERMISSIONS['user']:
        assign(perm[0], user, user)