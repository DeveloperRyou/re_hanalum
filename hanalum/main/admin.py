from django.contrib import admin
from .models import Sidebar_category
from .models import Sidebar_unit
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['menu_name', 'menu_url', 'menu_authority', 'menu_sort',]

class UnitAdmin(admin.ModelAdmin):
    list_display = ['menu_name', 'menu_url', 'menu_authority', 'menu_sort', 'upper_category']

admin.site.register(Sidebar_category, CategoryAdmin)
admin.site.register(Sidebar_unit, UnitAdmin)

