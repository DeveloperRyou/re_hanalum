from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    #pub_writer
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = RichTextField()
    #authority
    #num_view
    #num_comment
    #num_good
    #num_bad
    #file_1
    #file_2
    #file_3
