from django.contrib.auth.decorators import user_passes_test


def regular_user_required(function):
    """
    Requires regular user.
    
    """
    actual_decorator = user_passes_test(lambda user: user.profile.is_regular())
    if function:
        return actual_decorator(function)
    return actual_decorator


def manager_user_required(function):
    """
    Requires manager user.
    
    """
    actual_decorator = user_passes_test(lambda user: user.profile.is_manager())
    if function:
        return actual_decorator(function)
    return actual_decorator