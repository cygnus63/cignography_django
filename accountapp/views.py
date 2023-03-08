from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy

# from accountapp.models import Texts
# Create your views here.

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('main:intro')
    template_name = 'create.html'

from django.http import HttpResponse, HttpResponseRedirect

from accountapp.forms import AccountUpdateForm
from accountapp.decorators import account_ownership_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

has_ownership = [
    account_ownership_required, login_required
]

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('main:intro')
    # reverse_lazy는 함수와 클래스의 불러오는 방식이 달라짐. 클래스에서 reverse를 사용할 수 없음.
    template_name = 'accountapp/create.html'
    # 어느 html을 쓸지.

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

# @method_decorator(has_ownership, 'get')
# @method_decorator(has_ownership, 'post')

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'

# @method_decorator(has_ownership, 'get')
# @method_decorator(has_ownership, 'post')

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('main:intro')
    template_name = 'accountapp/delete.html'