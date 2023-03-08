from django.urls import path
from guestbook.views import CommentCreateView, CommentListView, CommentDeleteView, Comment
from django.views.generic import TemplateView

app_name = "guestbook"

urlpatterns = [
        path('', CommentListView.as_view(), name='guestbook'),
        path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
        path('create/', CommentCreateView.as_view(), name='create'),
        # path('', TemplateView.as_view(template_name='guestbook/guestbook.html'), name='guestbook'),

]