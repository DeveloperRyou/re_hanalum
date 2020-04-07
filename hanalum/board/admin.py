from django.contrib import admin

from .models import Board

class BoardAdmin(admin.ModelAdmin):
    list_display = ['board_id', 'title', 'auth_read', 'auth_write', 'use_comment', 'use_good', 'use_bad', 'use_anony',]

admin.site.register(Board, BoardAdmin)