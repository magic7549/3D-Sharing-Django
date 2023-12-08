from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from ..models import Post


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    search_filter = request.GET.get('filter', '1')  # 검색 필터
    post_list = Post.objects.order_by('-create_date')
    
    if kw:
        if search_filter == '1':  # 제목 + 내용 검색
            post_list = post_list.filter(
                Q(title__icontains=kw) |
                Q(content__icontains=kw)
            ).distinct()
        elif search_filter == '2':  # 제목 검색
            post_list = post_list.filter(
                Q(title__icontains=kw)
            ).distinct()
        elif search_filter == '3':  # 내용 검색
            post_list = post_list.filter(
                Q(content__icontains=kw)
            ).distinct()
        elif search_filter == '4':  # 작성자 검색
            post_list = post_list.filter(
                Q(author__username__icontains=kw)
            ).distinct()
        elif search_filter == '5':  # 댓글 검색
            post_list = post_list.filter(
                Q(comment__content__icontains=kw) |
                Q(comment__author__username__icontains=kw)
            ).distinct()
    
    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj, 'page': page, 'kw': kw, 'search_filter': search_filter}
    return render(request, 'community/post_list.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'community/post_detail.html', context)