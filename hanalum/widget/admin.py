from django.contrib import admin

from .models import CalendarEvent

class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ['start_at', 'end_at', 'eventname']


admin.site.register(CalendarEvent, CalendarEventAdmin)