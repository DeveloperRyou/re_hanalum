from django.db import models
from hanalum import settings

class Sidebar(models.Model):
    menu_name = models.CharField( #메뉴이름
        verbose_name='Menu_name',
        max_length=20,
    )
    menu_url = models.URLField( #메뉴링크
        'url',
        blank=True,
        null=True,
    )
    page_authority = models.IntegerField( #접근권한
        verbose_name='page_authority',
        default=0,
    )
    unit = models.BooleanField( #대단원소단원
        verbose_name='unit',
    )


