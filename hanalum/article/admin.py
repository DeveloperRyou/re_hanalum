from django.contrib import admin

from .forms import ArticleCreationForm
from .models import Article

class ArticleAdmin():
    form = ArticleCreationForm
    list_display = ['title', 'content',]

admin.site.register(Article)