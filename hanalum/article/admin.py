from django.contrib import admin

from .forms import ArticleCreationForm
from .models import Article
from .models import Like

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_user', 'pub_date']
    list_filter = ['pub_user', 'pub_date', ]

admin.site.register(Article, ArticleAdmin)

class LikeAdmin(admin.ModelAdmin):
    list_display = ['num_good',]

admin.site.register(Like, LikeAdmin)
