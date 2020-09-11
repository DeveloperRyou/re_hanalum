from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['email', 'nickname', 'realname', 'gender', 'avatar',  'is_admin', 'is_active', 'authority']
    list_filter = ['is_admin',]
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('nickname', 'realname', 'gender', 'avatar')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'authority')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email','password1', 'password2')}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)