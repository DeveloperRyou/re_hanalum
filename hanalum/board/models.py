from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class Board(models.Model):
    board_id = models.CharField(
        verbose_name='Board_id',
        max_length=100,
    )
    title = models.CharField(
        verbose_name='Title',
        max_length=100,
    )
    auth_read = models.IntegerField(
        verbose_name='Auth_read',
        default=0,
    )
    auth_write = models.IntegerField(
        verbose_name='Auth_write',
        default=0,
    )
    use_comment = models.BooleanField(
        verbose_name='Use_comment',
        default=True,
    )
    use_good = models.BooleanField(
        verbose_name='Use_good',
        default=True,
    )
    use_bad = models.BooleanField(
        verbose_name='Use_bad',
        default=True,
    )
    use_anony = models.BooleanField(
        verbose_name='Use_anony',
        default=False,
    )

    priority = models.IntegerField(
        verbose_name='priority',
        default=0
    )

    represent_color = ColorField(
        default='#FF0000'
    )

    def __str__(self):
        return self.title