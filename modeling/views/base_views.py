from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from ..models import Modeling


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    search_filter = request.GET.get('filter', '1')  # 검색 필터
    extension_type = request.GET.get('extension', '1') # 확장자
    modeling_list = Modeling.objects.order_by('-create_date')

    if kw:
        if search_filter == '1':  # 제목 + 내용 검색
            modeling_list = modeling_list.filter(
                Q(title__icontains=kw) |
                Q(description__icontains=kw)
            ).distinct()
        elif search_filter == '2':  # 제목 검색
            modeling_list = modeling_list.filter(
                Q(title__icontains=kw)
            ).distinct()
        elif search_filter == '3':  # 내용 검색
            modeling_list = modeling_list.filter(
                Q(description__icontains=kw)
            ).distinct()
        elif search_filter == '4':  # 작성자 검색
            modeling_list = modeling_list.filter(
                Q(author__username__icontains=kw)
            ).distinct()

    if extension_type != '1':  # 확장자가 'all'이 아닌 경우에만 필터링
        if extension_type == '2':  # 'fbx'
            modeling_list = modeling_list.filter(model_extension='fbx')
        elif extension_type == '3':  # 'glb'
            modeling_list = modeling_list.filter(model_extension='glb')        
    
    paginator = Paginator(modeling_list, 30)  # 페이지당 30개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'modeling_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'modeling/modeling_list.html', context)


def detail(request, modeling_id):
    modeling = get_object_or_404(Modeling, pk=modeling_id)
    context = {'modeling': modeling}
    return render(request, 'modeling/modeling_detail.html', context)
