from django.http import HttpResponseForbidden
from photoapp.models import Image

def image_ownership_required(func):
    def decorated(request, *args, **kwargs):
        image = Image.objects.get(pk=kwargs['pk'])
        if not image.writer == request.user:
            return HttpResponseForbidden()
        
        return func(request, *args, **kwargs)
    
    return decorated

def is_superuser(func):
    def decorated(request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        
        return func(request, *args, **kwargs)
    
    return decorated
