from django.contrib import admin
from .models import Sidebar
# Register your models here.

class SidebarAdmin(admin.ModelAdmin):
    list_display = ['menu_name', 'menu_url', 'page_authority', 'unit',]
    list_filter = ['unit',]
admin.site.register(Sidebar, SidebarAdmin)

