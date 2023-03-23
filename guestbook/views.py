from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from guestbook.models import Comment
from guestbook.forms import CommentCreationForm
from django.views.generic.edit import FormMixin
from django.utils.decorators import method_decorator
from guestbook.decorators import is_yours

import telegram

def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read().rstrip().lstrip()
    file.close()

    return secret

def telegram_send(writer, message):

    bot = telegram.Bot(token=read_secret('CGN_TG_TOKEN'))
    link = 'https://cigno.kr/guestbook/'
    button = [[telegram.InlineKeyboardButton('자세히 보기', url = link)]]
    reply_markup = telegram.InlineKeyboardMarkup(button)

    bot.sendMessage(chat_id=read_secret('MY_TG_ID'), 
                    text = f'{writer} : {message}', 
                    reply_markup = reply_markup)

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    context_object_name = 'target_comment'
    template_name = 'guestbook/create.html'


    def form_valid(self, form):
        temp_comment = form.save(commit=False)

        writer = temp_comment.writer
        message = temp_comment.comment

        print(writer + message)

        # telegram_send(writer, message)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('guestbook:guestbook')

class CommentListView(ListView, FormMixin):
    model = Comment
    ordering = '-id'
    form_class = CommentCreationForm
    context_object_name = 'comment_list'
    template_name = 'guestbook/list.html'
    paginate_by = 10

@method_decorator(is_yours, 'post')

class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('guestbook:guestbook')
    context_object_name = 'target_comment'
    template_name = 'guestbook/delete.html'






