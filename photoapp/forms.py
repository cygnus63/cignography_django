from django.forms import ModelForm

from photoapp.models import Image

class ImageCreationForm(ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image', 'content']