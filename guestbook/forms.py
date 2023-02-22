from django.forms import ModelForm

from guestbook.models import Comment

class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['writer', 'password', 'content']