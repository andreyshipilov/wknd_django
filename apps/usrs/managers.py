from django.contrib.auth.models import User, UserManager


class ProfileManager(UserManager):
    """
    Extra functionality for the Profile model.
    """

    def create_user(self, username, email, password, first_name, last_name,
                    active=False, send_email=True):
        #now = get_datetime_now()

        new_user = User.objects.create_user(username, email, password)
        new_user.is_active = active
        new_user.save()

        userena_profile = self.create_userena_profile(new_user)

        # All users have an empty profile
        profile_model = get_profile_model()
        try:
            new_profile = new_user.get_profile()
        except profile_model.DoesNotExist:
            new_profile = profile_model(user=new_user)
            new_profile.save(using=self._db)

        # Give permissions to view and change profile
        for perm in ASSIGNED_PERMISSIONS['profile']:
            assign(perm[0], new_user, new_profile)

        # Give permissions to view and change itself
        for perm in ASSIGNED_PERMISSIONS['user']:
            assign(perm[0], new_user, new_user)

        if send_email:
            userena_profile.send_activation_email()

        return new_user