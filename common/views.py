from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from common.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '회원가입에 성공하였습니다.')
            return render(request, 'common/login.html')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


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


@login_required(login_url='common:login')
def delete(request):
    if request.method == 'POST':
        password = request.POST.get('password')

        # 비밀번호 확인
        user = authenticate(username=request.user.username, password=password)

        if user is not None:
            # 비밀번호가 일치하면 회원을 삭제하고 로그아웃
            user.delete()
            messages.success(request, '회원탈퇴를 하였습니다.')
            logout(request)
            return render(request, 'common/login.html')
        else:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return render(request, 'mypage/mypage_delete.html')
    else:
        return render(request, 'mypage/mypage_delete.html')
    