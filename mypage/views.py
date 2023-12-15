from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from common.views import change_password

from modeling.models import Modeling
from community.models import Post


@login_required(login_url='common:login')
def index(request):
    return mypage_change_password(request)


@login_required(login_url='common:login')
def mypage_change_password(request):
    return change_password(request)


@login_required(login_url='common:login')
def delete(request):
    return render(request, 'mypage/mypage_delete.html')


@login_required(login_url='common:login')
def my_post(request):
    modeling_list = Modeling.objects.filter(author=request.user)
    post_list = Post.objects.filter(author=request.user).order_by('-create_date')
    context = {'modeling_list': modeling_list, 'post_list': post_list}
    return render(request, 'mypage/mypage_post.html', context)