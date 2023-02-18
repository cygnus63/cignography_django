from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from photoapp.forms import ImageCreationForm
from photoapp.models import Image
from photoapp.decorators import image_ownership_required

# Create your views here.

def photo(request):
    return render(request, 'photoapp/photos.html')

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')

class ImageCreateView(CreateView):
    model = Image
    form_class = ImageCreationForm
    template_name = 'photoapp/create.html'

    def form_valid(self, form):
        # print(self.request.user)
        temp_image = form.save(commit=False)
        temp_image.writer = self.request.user
        temp_image.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('photoapp:detail', kwargs={'pk': self.object.pk})

class ImageDetailView(DetailView):
    model = Image
    context_object_name = 'target_image'
    template_name = 'photoapp/detail.html'

@method_decorator(image_ownership_required, 'get')
@method_decorator(image_ownership_required, 'post')

class ImageUpdateView(UpdateView):
    model = Image
    context_object_name = 'target_image'
    form_class = ImageCreationForm
    template_name = 'photoapp/update.html'

    def get_success_url(self):
        return reverse ('photoapp:detail', kwargs={'pk': self.object.pk})