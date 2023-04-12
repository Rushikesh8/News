from django.db import models
from django.contrib.auth.models import User

def upload_image(instance, filename):
    return f'images/{filename}'

class News(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    date = models.CharField(max_length=12)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)
    source = models.CharField(max_length=100)
