"""hanalum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import login.views
import article.views
import member.views
import board.views
import widget.views
import main.views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login.views.login, name='login'),
    path('main/', main.views.main, name='main'),
    path('article/<int:article_id>', article.views.article, name='article/<int:article_id>'),
    path('write/', article.views.write, name='write'),
    path('register/', member.views.register, name='register'),
    path('agree/', member.views.agree, name='agree'),
    path('board/', board.views.board, name='board'),
    path('calendar/', widget.views.calendar, name='widget'),
    path('cafeteria/', widget.views.cafeteria, name='widget'),
    path('acadnotice/', widget.views.acadnotice, name='widget'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
