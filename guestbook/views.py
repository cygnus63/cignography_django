from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from guestbook.models import Comment
from guestbook.forms import CommentCreationForm
from django.views.generic.edit import FormMixin
from django.utils.decorators import method_decorator
from guestbook.decorators import is_yours



class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    context_object_name = 'target_comment'
    template_name = 'guestbook/create.html'

    # def form_valid(self, form):
    #     temp_comment = form.save(commit=False)
    #     temp_comment.save()

    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse('guestbook:guestbook')

class CommentListView(ListView, FormMixin):
    model = Comment
    ordering = '-date'
    form_class = CommentCreationForm
    context_object_name = 'comment_list'
    template_name = 'guestbook/list.html'
    paginatio_by = 30

@method_decorator(is_yours, 'post')

class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('guestbook:guestbook')
    context_object_name = 'target_comment'
    template_name = 'guestbook/delete.html'






