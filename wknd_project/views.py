import sys
from django.template import loader, Context
from django.http import HttpResponseServerError



def custom_500(request):
    t = loader.get_template('500.html')
    type, value, tb = sys.exc_info()
    return HttpResponseServerError(t.render(Context({
       'EV': value,
    })))