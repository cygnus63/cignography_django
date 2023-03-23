from django.contrib import admin

# Register your models here.
from guestbook.models import Comment

admin.site.register(Comment)