from django.forms import ModelForm

from photoapp.models import Image

class ImageCreationForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'content']

    def __str__(self) -> str:
        return f'{self.pk}'

