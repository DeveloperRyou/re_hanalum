from django.contrib import admin

from .models import Article
from .models import Like
from .models import Dislike
from .models import Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'board_type','pub_user', 'created_at', 'like_count', 'dislike_count', 'is_popup']
    list_filter = ['created_at', ]


admin.site.register(Article, ArticleAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'article']


admin.site.register(Like, LikeAdmin)


class DislikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'article'] 


admin.site.register(Dislike, DislikeAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['pub_user', 'article_type', 'content', 'created_at', 'authority']


admin.site.register(Comment, CommentAdmin)
