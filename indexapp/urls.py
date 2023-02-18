from django.urls import path
from indexapp.views import intro

app_name = 'indexapp'

urlpatterns = [
    path('', intro, name='intro')
]
