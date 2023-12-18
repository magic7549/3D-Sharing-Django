from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from common.views import change_password

from modeling.models import Modeling
from community.models import Post


@login_required(login_url='common:login')
def index(request):
    return redirect('mypage:change_password')


@login_required(login_url='common:login')
def mypage_change_password(request):
    return change_password(request)


@login_required(login_url='common:login')
def delete(request):
    return render(request, 'mypage/mypage_delete.html')


@login_required(login_url='common:login')
def my_post(request):
    modeling_list = Modeling.objects.filter(author=request.user)

    page = request.GET.get('page', '1')  # 페이지
    post_list = Post.objects.filter(author=request.user).order_by('-create_date')
    paginator = Paginator(post_list, 10)
    page_post = paginator.get_page(page)
    context = {'modeling_list': modeling_list, 'post_list': page_post}
    return render(request, 'mypage/mypage_post.html', context)


@login_required(login_url='common:login')
def my_modeling(request):
    page = request.GET.get('page', '1')  # 페이지
    modeling_list = Modeling.objects.filter(author=request.user)
    paginator = Paginator(modeling_list, 12)  # 페이지당 12개씩 보여주기
    page_modeling = paginator.get_page(page)
    context = {'modeling_list': page_modeling}
    return render(request, 'mypage/mypage_modeling.html', context)


@login_required(login_url='common:login')
def my_community(request):
    page = request.GET.get('page', '1')  # 페이지
    post_list = Post.objects.filter(author=request.user).order_by('-create_date')
    paginator = Paginator(post_list, 10)
    page_community = paginator.get_page(page)
    context = {'post_list': page_community}
    return render(request, 'mypage/mypage_community.html', context)