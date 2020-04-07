from django.db import models


class Sidebar_category(models.Model):
    menu_name = models.CharField(  # 메뉴이름
        verbose_name='Menu_name',
        max_length=20,
    )
    menu_url = models.URLField(  # 메뉴링크
        verbose_name='Menu_url',
        blank=True,
        null=True,
    )
    menu_authority = models.IntegerField(  # 접근권한
        verbose_name='Menu_authority',
        default=0,
    )
    menu_sort = models.IntegerField(  # 출력순서
        verbose_name='Menu_sort',
        default=0,
    )

    def __str__(self):
        return self.menu_name


class Sidebar_unit(models.Model):
    menu_name = models.CharField( # 메뉴이름
        verbose_name='Menu_name',
        max_length=20,
    )
    menu_url = models.URLField( # 메뉴링크
        verbose_name='Menu_url',
        blank=True,
        null=True,
    )
    menu_authority = models.IntegerField( # 접근권한
        verbose_name='Menu_authority',
        default=0,
    )
    menu_sort = models.IntegerField( # 출력순서
        verbose_name='Menu_sort',
        default=0,
    )
    upper_category = models.ForeignKey( #연결된 카테고리 정보
        Sidebar_category,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.menu_name


