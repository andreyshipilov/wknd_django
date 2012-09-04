from django.contrib import admin

from .models import *


class PlaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'address')
admin.site.register(Place, PlaceAdmin)


class VenueAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('slug',)
    list_display = ('title', 'place', 'date_time',)
admin.site.register(Venue, VenueAdmin)

admin.site.register(Genre)


#class ProfileAdmin(admin.ModelAdmin):
#    list_display = ('user', 'user_type')
# Already registered in Userena. So unregister it.
#admin.site.unregister(Profile)
#admin.site.register(Profile, ProfileAdmin)

#admin.site.register(Regular)
#admin.site.register(Manager)