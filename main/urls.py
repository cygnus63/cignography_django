from django.urls import path
from main.views import intro
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', intro, name='intro')
]

