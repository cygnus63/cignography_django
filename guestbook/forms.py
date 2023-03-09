from django.forms import ModelForm

from guestbook.models import Comment
from django import forms

class CommentCreationForm(ModelForm):    
    label_suffix = ''  # 필드 라벨 숨기기

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['writer'].label = False
        self.fields['password'].label = False
        self.fields['comment'].label = False

    class Meta:
        model = Comment
        fields = ['writer', 'password', 'comment']        
        widgets = {
            'writer': forms.TextInput(
                attrs={
                    'class': 'form-control d-inline-block mr-2',
                    'placeholder': '작성자',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control d-inline-block mr-2',
                    'placeholder': '비밀번호'
                }
            ),

            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',    
                    'placeholder': '※ 위 비밀번호는 삭제하는데에 사용되므로 주로 사용하는 비밀번호는 지양해주세요 :)',
                    'rows': 5
                }
            )
        }