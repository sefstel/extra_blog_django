from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from os import path


class Post(models.Model):
    post_label = models.CharField(max_length=50)
    post_small_text = models.CharField(max_length=300)
    post_text = models.CharField(max_length=1000,blank=True)
    create_as = models.DateTimeField(default=timezone.now)
    post_image = models.ImageField(upload_to='vodopad')
    published = models.BooleanField(default=False)
    post_url = models.SlugField(max_length=50,default='#')


    def __str__(self):
        return self.post_label

class Comments(models.Model):
    name = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatar')
    content = models.TextField(max_length=300)
    reply = models.ForeignKey('self',verbose_name='Родитель', on_delete=models.SET_NULL,blank=True,null=True)
    date = models.DateTimeField(default=timezone.now)
    post_ref = models.ForeignKey(Post,on_delete=models.CASCADE)