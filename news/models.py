from django.db import models
from time import strftime


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False)
    about = models.TextField(max_length=256, null=False)
    content = models.TextField(max_length=1024, null=False)
    author = models.CharField(max_length=100, null=False)
    image = models.FileField(null=False, upload_to='upload/')
    published = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M:%S'))
    source = models.URLField(null=True)
