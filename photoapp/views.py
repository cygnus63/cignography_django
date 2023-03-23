from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from photoapp.forms import ImageCreationForm
from photoapp.models import Image
from photoapp.decorators import image_ownership_required, is_superuser


from PIL import Image as PI

def photo(request):
    return render(request, 'photoapp/photos.html')

@method_decorator(is_superuser, 'get')
@method_decorator(is_superuser, 'post')

class ImageCreateView(CreateView):
    model = Image
    form_class = ImageCreationForm
    template_name = 'photoapp/create.html'

    def form_valid(self, form):

        temp_image = form.save(commit=False)
        temp_image.writer = self.request.user
        temp_image.save()

        uploaded_image = temp_image.image
        img = PI.open(uploaded_image.path)

        maxSize = 2048

        if img.width > img.height:
            width = maxSize
            height = int(maxSize * img.height / img.width)
        else:
            width = int(maxSize * img.width / img.height)
            height = maxSize

        resized_image = img.resize((width, height))

        logo_img = PI.open('static/logo_white.png',)
        logo_img = logo_img.resize((120, 30))

        alpha = logo_img.split()[3]
        alpha = PI.eval(alpha, lambda a: int(a * 0.4))
        logo_img.putalpha(alpha)

        logo_width, logo_height = logo_img.size
        x = (resized_image.width - logo_width) // 2
        y = resized_image.height - logo_height - 70
        resized_image.paste(logo_img, (x, y), logo_img)

        resized_image.save(uploaded_image.path)

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

class ImageListView(ListView):
    model = Image
    ordering = '-id'
    context_object_name = 'photo_list'
    template_name = 'photoapp/list.html'
    paginate_by = 25

@method_decorator(image_ownership_required, 'get')
@method_decorator(image_ownership_required, 'post')

class ImageDeleteView(DeleteView):
    model = Image
    success_url = reverse_lazy('photoapp:list')
    context_object_name = 'target_image'
    template_name = 'photoapp/delete.html'