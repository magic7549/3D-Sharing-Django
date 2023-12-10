from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from ..models import ContestRoundInfo, Contest, PreviousContest
from modeling.models import Modeling
from ..tasks import create_new_round


@login_required(login_url='common:login')
def index(request):
    current_round_info = ContestRoundInfo.objects.latest('round_num')
    current_date = timezone.now().date()
    days_until_vote = (current_round_info.vote_date - current_date).days
    days_until_end = (current_round_info.end_date - current_date).days

    # 만약 현재 날짜가 대회 종료된 이후라면 새로운 대회 회차 생성
    if (days_until_end < 0):
        create_new_round()
        current_round_info = ContestRoundInfo.objects.latest('round_num')
        days_until_vote = (current_round_info.vote_date - current_date).days
        days_until_end = (current_round_info.end_date - current_date).days

    previous_contest = PreviousContest.objects.all()
    my_models = Modeling.objects.filter(author=request.user)

    context = {
        'current_round_info': current_round_info,
        'days_until_vote': days_until_vote,
        'days_until_end': days_until_end,
        'previous_contest': previous_contest,
        'my_models': my_models,
    }
    return render(request, 'contest/contest_home.html', context)


@login_required(login_url='common:login')
def registerContest(request, modeling_id):
    current_round_info = ContestRoundInfo.objects.latest('round_num')
    modeling = get_object_or_404(Modeling, id=modeling_id)

    # 현재 라운드에 모델링이 이미 참가했는지 확인
    current_models = Contest.objects.filter(round_info=current_round_info, modeling=modeling)

    if current_models.exists():
        messages.error(request, '이미 참가한 모델입니다.')
    else:
        # 등록 절차 수행
        contest_instance = Contest(round_info=current_round_info, modeling=modeling)
        contest_instance.save()
        messages.success(request, '참가 신청이 완료되었습니다.')
    
    return redirect('contest:index')


@login_required(login_url='common:login')
def contest_vote(request, modeling_id):
    current_round_info = ContestRoundInfo.objects.latest('round_num')
    modeling = get_object_or_404(Modeling, id=modeling_id)
    current_models = Contest.objects.filter(round_info=current_round_info, modeling=modeling)
    
    if current_models.exists():
        contest_instance = current_models.first()

        if request.user == contest_instance.modeling.author:
            messages.error(request, '본인이 작성한 모델은 추천할 수 없습니다.')
        else:
            contest_instance.voter.add(request.user)
            messages.success(request, '추천하였습니다.')
    else:
        messages.error(request, '해당 모델이 대회에 등록되어 있지 않습니다.')
        
    return redirect('contest:index')


@login_required(login_url='common:login')
def get_data(request, offset):
    current_round_info = ContestRoundInfo.objects.latest('round_num')
    current_date = timezone.now().date()
    days_until_vote = (current_round_info.vote_date - current_date).days

    offset = int(offset)
    data = Contest.objects.filter(round_info=current_round_info)[offset:offset+3]
    data_list = [{'id': item.modeling.id, 'title': item.modeling.title, 'author': item.modeling.author.username, 'thumbnail': item.modeling.thumbnail.url, 'days_until_vote': days_until_vote, 'voter_count': item.voter.count()} for item in data]

    return JsonResponse({'data': data_list})