USER_TYPES = (
   (1, 'Regular user'),
   (2, 'Place manager'),
)
ACTIVATED = u"ALREADY_ACTIVATED" # String set when user is activated
ACTIVATION_DAYS = 7
FORBIDDEN_USERNAMES = ('signup', 'signout', 'signin', 'activate', 'me',
                       'password', 'admin', 'agora', 'staff', 'agoraciudadana',
                       'agoravoting', 'root', 'administrator', 'adminstrador',
                       'hostmaster', 'info', 'ssladmin', 'sysadmin', 'webmaster',
                       'no-reply', 'mail', 'email', 'accounts', 'misc', 'api',
                       'e-mail', 'wknd')