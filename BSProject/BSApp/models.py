from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title=models.TextField(max_length=50)
    content=models.CharField(max_length=500)
    time=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(blank=True,max_length=30)

    def __str__(self):
        return self.title
