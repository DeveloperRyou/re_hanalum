from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from datetime import datetime


# 모델 migrate 할 때 setting의 'django.contrib.admin', urls의 path('admin/', admin.site.urls) 주석처리하기
class UserManager(BaseUserManager):
    # 유저 클래스를 관리하는 클래스
    def _create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('이메일은 필수입니다')
        user = self.model(
            email=self.normalize_email(email),
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)

    def create_user(self, email, password=None, **kwargs):
        kwargs.setdefault('is_admin', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_admin', True)
        kwargs.setdefault('is_superuser', True)
        return self._create_user(email, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    # 유저 클래스 (DB 생성)
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(
        verbose_name='Nickname',
        max_length=30,
        unique=True,
    )
    realname = models.CharField(
        verbose_name='Realname',
        max_length=30,
    )
    GENDER_CHOICES = (
        ('M', '남'),
        ('F', '여'),
    )
    gender = models.CharField(
        verbose_name='Gender',
        max_length=2,
        choices=GENDER_CHOICES,
    )
    authority = models.IntegerField(
        verbose_name='Authority',
        default=1,
    )
    avatar = models.ImageField(
        verbose_name='avatar',
        upload_to='avatars/',
        null=True,
        blank=True,
    )
    temp_list = []
    for year in range(2014, datetime.today().year + 1):
        temp_list.append((year, str(year)))
    ADMISSION_YEAR_CHOICES = tuple(temp_list)
    admission_year = models.IntegerField(
        verbose_name='Admission_year',
        choices=ADMISSION_YEAR_CHOICES,
        # 밑에 두 줄은 나중에 삭제해야 함
        null=True,
        blank=True,
    )
    date_joined = models.DateTimeField(
        verbose_name='Date joined',
        auto_now_add=True,
    )
    is_active = models.BooleanField(
        verbose_name='Is active',
        default=True,
    )
    is_admin = models.BooleanField(
        verbose_name='Is admin',
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'realname', 'gender', ]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ('-date_joined',)

    def __str__(self):
        return self.nickname

    def get_email(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_superuser
