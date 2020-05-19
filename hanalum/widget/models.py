from django.db import models

# Create your models here.

class CalendarEvent(models.Model):
    start_at = models.DateTimeField(
        verbose_name='Start',

    )
    end_at = models.DateTimeField(
        verbose_name='End',
    )
    eventname = models.CharField(
        verbose_name='Eventname',
        max_length=30,
    )
