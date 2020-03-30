from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from member.models import User
from hanalum import settings
import os

# Create your models here.
class Article(models.Model):
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
    ) # 값이 -1이면 비추, 1이면 추