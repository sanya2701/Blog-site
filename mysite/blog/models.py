from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    author= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    descrip= models.TextField()
    created_date= models.DateTimeField(default=timezone.now)
    published= models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def publish(self):
        self.published=True
        self.save()

class Comment(models.Model):
    post=models.ForeignKey('blog.Post',on_delete=models.CASCADE,related_name="comments")
    author=models.CharField(max_length=200)
    desc= models.TextField(max_length=500)
    created_date= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.desc
