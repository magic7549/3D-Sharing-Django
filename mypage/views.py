from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='common:login')
def index(request):
    return change_password(request)


@login_required(login_url='common:login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '비밀번호 변경에 성공하였습니다.')
            return redirect('mypage:index')
        else:
            old_password_errors = form.errors.get('old_password', None)
            new_password2_errors = form.errors.get('new_password2', None)

            if old_password_errors:
                messages.error(request, old_password_errors[0])
            elif new_password2_errors:
                messages.error(request, new_password2_errors[0])

            return redirect('mypage:index')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'mypage/mypage_password.html', {'form': form})