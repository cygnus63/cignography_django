from django.db import models

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    password = models.CharField(max_length=32, null=False, blank=False)
    comments  = models.TextField(max_length=200, null=False, blank=False)
    date = models.DateField(auto_now_add=True, null=False)
