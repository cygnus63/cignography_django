from django.db import models

# Create your models here.

class Comment(models.Model):
    writer = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=32, null=False, blank=False)
    comment = models.TextField(max_length=200, null=False, blank=False)
    date = models.DateField(auto_now_add=True, null=False)
