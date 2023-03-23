from django.contrib.auth.models import User
from django.db import models
import random

def media_directory_path(instance, filename):
    random_number = random.randint(10**14, 10**15-1)
    random_string = str(random_number).zfill(15)

    return f"images/{random_string}.jpg"

class Image(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='image', null=True)
    image = models.ImageField(null=False, upload_to=media_directory_path)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True)
