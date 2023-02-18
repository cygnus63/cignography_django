from django.urls import path
from photoapp.views import photo
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from photoapp.views import ImageCreateView, ImageDetailView, ImageUpdateView

app_name = 'photoapp'

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'photoapp/photos.html' ), name='photo'),
    path('create/', ImageCreateView.as_view(), name = 'create'),
    path('detail/<int:pk>', ImageDetailView.as_view(), name = 'detail'),
    path('update/<int:pk>', ImageUpdateView.as_view(template_name = 'update.html'), name = 'update'),
]

