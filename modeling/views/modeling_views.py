import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import ModelingForm
from ..models import Modeling

@login_required(login_url='common:login')
def modeling_create(request):
    if request.method == 'POST':
        form = ModelingForm(request.POST, request.FILES)
        if form.is_valid():
            modeling = form.save(commit=False)
            modeling.model_extension = os.path.splitext(request.FILES['model_file'].name)[1].lstrip('.')
            modeling.author = request.user
            modeling.create_date = timezone.now()
            modeling.save()
            return redirect('modeling:index')
    else:
        form = ModelingForm()
    context = {'form': form}
    return render(request, 'modeling/modeling_form.html', context)


@login_required(login_url='common:login')
def modeling_modify(request, modeling_id):
    modeling = get_object_or_404(Modeling, pk=modeling_id)
    if request.user != modeling.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('modeling:detail', modeling_id=modeling.id)
    if request.method == "POST":
        form = ModelingForm(request.POST, request.FILES, instance=modeling)
        if form.is_valid():
            modeling = form.save(commit=False)
            modeling.modify_date = timezone.now()
            modeling.model_extension = os.path.splitext(request.FILES['model_file'].name)[1].lstrip('.')
            modeling.save()
            return redirect('modeling:detail', modeling_id=modeling.id)
    else:
        form = ModelingForm(instance=modeling)
    context = {'form': form}
    return render(request, 'modeling/modeling_form.html', context)


@login_required(login_url='common:login')
def modeling_delete(request, modeling_id):
    modeling = get_object_or_404(Modeling, pk=modeling_id)
    if request.user != modeling.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('modeling:detail', modeling_id=modeling.id)
    modeling.delete()
    return redirect('modeling:index')


@login_required(login_url='common:login')
def modeling_vote(request, modeling_id):
    modeling = get_object_or_404(Modeling, pk=modeling_id)
    if request.user == modeling.author:
        messages.error(request, '본인이 작성한 모델은 추천할 수 없습니다.')
    else:
        modeling.voter.add(request.user)
    return redirect('modeling:detail', modeling_id=modeling.id)