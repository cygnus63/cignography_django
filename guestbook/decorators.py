from django.http import HttpResponseForbidden
from guestbook.models import Comment

def is_yours(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        passcode = request.POST.get('password')

        if comment.password != passcode:
            return HttpResponseForbidden('Password is incorrect')

        return func(request, *args, **kwargs)
    
    return decorated
