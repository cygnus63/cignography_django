from django.contrib.auth.models import User
from django.db import models

class Image(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='image', null=True)
    image = models.ImageField(null=False, upload_to="images/")
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    # 생성됐을때 자동으로 날짜 생성
