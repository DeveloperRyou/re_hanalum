from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from member.models import User
from board.models import Board
from django.utils import timezone
from hanalum import settings
import os

# Create your models here.
class Article(models.Model):
    board_type = models.ForeignKey(
        Board,
        on_delete=models.CASCADE
    )
    pub_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(
        verbose_name='Pub_date',
        auto_now_add=True,
    )
    title = models.CharField(
        verbose_name='Title',
        max_length=100,
    )
    content = RichTextUploadingField(
        verbose_name='Content',
    )
    num_view = models.IntegerField(
        verbose_name='Num_view',
        default=0,
    )
    num_comment = models.IntegerField(
        verbose_name='Num_comment',
        default=0,
    )
    """like_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='like_user_set',
        through='Like',
    )
    likes = models.ManyToManyField(
        User,
        verbose_name='likes',
    )"""
    num_good = models.IntegerField(
        verbose_name='Num_good',
        default=0,
    )
    num_bad = models.IntegerField(
        verbose_name='Num_bad',
        default=0,
    )
    file_1 = models.FileField(
        verbose_name='File_1',
        blank=True,
        null=True,
        upload_to="files/%Y/%m/%d"
    )
    file_2 = models.FileField(
        verbose_name='File_1',
        blank=True,
        null=True,
        upload_to="files/%Y/%m/%d"
    )
    file_3 = models.FileField(
        verbose_name='File_1',
        blank=True,
        null=True,
        upload_to="files/%Y/%m/%d"
    )

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        try:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.file_1.path))
            os.remove(os.path.join(settings.MEDIA_ROOT, self.file_2.path))
            os.remove(os.path.join(settings.MEDIA_ROOT, self.file_3.path))
        except:
            pass
        super(Article, self).delete(*args, **kwargs)  # 원래의 delete 함수를 실행

    """
    def total_likes(self):
        return self.likes.count()"""
 
"""
class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    ) # 추천 할 user 정보
    article_type = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    ) # 추천 받을 article 정보
    num_good = models.IntegerField(
        verbose_name='Num_good',
        default=0,
    ) # 값이 -1이면 비추, 1이면 추"""
    
class Comment(models.Model):
    writer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    ) # 댓글 달 user 정보
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    ) # 댓글 달릴 article 정보
    content = models.TextField(
        verbose_name='Content',
        blank=True,
        max_length=2000,
    ) #댓글 내용
    authority = models.IntegerField(
        verbose_name='Authority',
        default=0,
    ) #댓글 읽기 권한
    created_at = models.DateTimeField(
        verbose_name='Created',
        auto_now_add=True,
    ) #생성 날짜
    updated_at = models.DateTimeField(
        verbose_name='Updated',
        auto_now=True,
    ) #수정 날짜