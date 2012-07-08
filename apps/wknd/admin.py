from django.contrib import admin

from .models import *


class PlaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'address')
admin.site.register(Place, PlaceAdmin)


class EventAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('slug',)
    list_display = ('title', 'place', 'date_time',)
admin.site.register(Event, EventAdmin)

admin.site.register(Genre)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type')
# Already registered in Userena. So unregister it.
admin.site.unregister(Profile)
admin.site.register(Profile, ProfileAdmin)