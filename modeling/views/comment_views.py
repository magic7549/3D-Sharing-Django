from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import CommentForm
from ..models import Modeling, Comment


@login_required(login_url='common:login')
def comment_create(request, modeling_id):
    modeling = get_object_or_404(Modeling, pk=modeling_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.modeling = modeling
            comment.save()
            return redirect('modeling:detail', modeling_id=modeling.id)
    else:
        form = CommentForm()
    context = {'modeling': modeling, 'form': form}
    return render(request, 'modeling/modeling_detail.html', context)


@login_required(login_url='common:login')
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('modeling:detail', modeling_id=comment.modeling.id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('modeling:detail', modeling_id=comment.modeling.id)
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'modeling/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제 권한이 없습니다.')
    else:
        comment.delete()
    return redirect('modeling:detail', modeling_id=comment.modeling.id)


@login_required(login_url='common:login')
def comment_vote(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        comment.voter.add(request.user)
    return redirect('modeling:detail', modeling_id=comment.modeling.id)