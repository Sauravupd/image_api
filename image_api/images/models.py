from django.db import models
from django.db.models.deletion import PROTECT
from django.utils import timezone
from django.contrib.auth.models import User


def image_path(instance,filename):
    return 'image/{0}'.format(filename)

class Tag(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Tags'

class Images(models.Model):

    class Meta:
        verbose_name_plural = 'Images'
   
    options = (
        ('active','Active'),
        ('deactivated','inactive')
    )

    Tag = models.ForeignKey(Tag,on_delete=PROTECT)
    title = models.CharField(max_length=40)
    alt = models.TextField(max_length=100,null=True)
    images = models.ImageField(upload_to = image_path)
    slug = models.SlugField(max_length=250,unique_for_date='created')
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=PROTECT,related_name='author')
    status = models.CharField(max_length=20,choices=options,default='active')


    