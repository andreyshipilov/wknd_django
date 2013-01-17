from django.contrib import admin

from .models import Venue, Event, Genre


class VenueAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'address')
admin.site.register(Venue, VenueAdmin)


class EventAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('title', 'venue',)
admin.site.register(Event, EventAdmin)

admin.site.register(Genre)


#class ProfileAdmin(admin.ModelAdmin):
#    list_display = ('user', 'user_type')
# Already registered in Userena. So unregister it.
#admin.site.unregister(Profile)
#admin.site.register(Profile, ProfileAdmin)

#admin.site.register(Regular)
#admin.site.register(Manager)