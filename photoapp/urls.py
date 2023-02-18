from django.urls import path
from photoapp.views import photo
from django.conf import settings
from django.conf.urls.static import static

app_name = 'photoapp'

urlpatterns = [
    path('', photo, name='photo')
]

