from django.contrib import admin
from django.urls import path
from django.urls import re_path
import login.views
import article.views
import article.views_comment
import member.views
import board.views
import widget.views
import main.views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib.auth.decorators import login_required
from ckeditor_uploader import views as views_ckeditor
from django.views.decorators.cache import never_cache 
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login.views.login, name='login'),
    path('logout/', login.views.logout, name='logout'),
    path('main/', main.views.main, name='main'),

    path('article/<int:article_id>', article.views.article, name='article'),
    path('article_write/<str:board_id>', article.views.article_write, name='article_write'),
    path('article_update/<int:article_id>', article.views.article_update, name='article_update'),
    path('article_delete/<int:article_id>', article.views.article_delete, name='article_delete'),
    path('popup/<int:article_id>', article.views.popup, name='popup'),

    path('like/', article.views.article_like, name='article_like'),
    path('dislike/', article.views.article_dislike, name = 'article_dislike'),

    path('comment_write/<int:article_id>', article.views_comment.comment_write, name='comment_write'),
    path('comment_update/<int:comment_id>', article.views_comment.comment_update, name='comment_update'),
    path('comment_delete/<int:comment_id>', article.views_comment.comment_delete, name='comment_delete'),
  
    re_path(r'^upload/', login_required(views_ckeditor.upload), name='ckeditor_upload'),
    re_path(r'^browse/', never_cache(login_required(views_ckeditor.browse)), name='ckeditor_browse'),


    path('register/', member.views.register, name='register'),
    path('agree/', member.views.agree, name='agree'),
    path('activate/<str:uidb64>/<str:token>/', member.views.activate, name="activate"),

    path('memberinfo/', member.views.memberinfo, name='memberinfo'),
    path('memberdelete/', member.views.memberdelete, name='memberdelete'),

    path('board/<str:board_id>/', board.views.board, name='board'),
    path('board/<str:board_id>/<int:page>/', board.views.board, name='board'),

    path('calendar/', widget.views.calendar, name='widget'),
    path('cafeteria/', widget.views.cafeteria, name='widget'),
    path('acadnotice/', widget.views.acadnotice, name='widget'),
    path('weekcalendar/', widget.views.weekcalendar, name='widget'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)