from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.triggers.cron import CronTrigger
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.utils import timezone
from .models import ContestRoundInfo, Contest, PreviousContest


def create_new_round():
    print("create_new_round_start")

    # 현재 회차 정보에서 마지막 회차 번호를 가져옵니다.
    try:
        current_round_info = ContestRoundInfo.objects.latest('round_num')
        new_round_num = current_round_info.round_num + 1
        current_round_end_date = current_round_info.end_date
    except ObjectDoesNotExist:
        # 데이터베이스에 해당 모델의 레코드가 없을 경우 처리할 내용
        new_round_num = 1  # 또는 다른 기본값 설정
        current_round_end_date = timezone.now().date() - timezone.timedelta(days=1)

    # 현재 시간
    today = timezone.now().date()

    # 만약 현재 시간이 end_date를 지났다면
    if today > current_round_end_date:
        # 이전 회차의 우승 작품을 PreviousContest로 이동
        if current_round_info:
            num = Contest.objects.filter(round_info=current_round_info).annotate(vote_count=Count('voter')).order_by('-vote_count').first().vote_count

            previous_winners = Contest.objects.annotate(num_votes=Count('voter')).filter(round_info=current_round_info, num_votes=num)
            
            for previous_winner in previous_winners:
                PreviousContest.objects.create(
                    contest_info = previous_winner
                )

        # 새로운 회차의 start_date, vote_date, end_date를 계산합니다.
        days_until_monday = (today.weekday() - 0) % 7  # 0은 월요일을 나타냄
        start_date = today - timezone.timedelta(days=days_until_monday)
        vote_date = start_date + timezone.timedelta(weeks=1)
        end_date = vote_date + timezone.timedelta(days=6)

        # 새로운 회차 정보를 생성합니다.
        ContestRoundInfo.objects.create(
            round_num=new_round_num,
            start_date=start_date,
            vote_date=vote_date,
            end_date=end_date,
        )

        print("create_new_round : " + str(new_round_num))

def start_scheduler():
    # 백그라운드 스케줄러를 생성합니다.
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # create_new_round 함수를 매 주 실행되도록 스케줄링합니다.
    scheduler.add_job(
        create_new_round,
        trigger=CronTrigger(
            day_of_week="mon", hour="00", minute="00"
        ),
        id="create_new_round",
        max_instances=1,
        replace_existing=True,
    )

    # 스케줄러를 시작합니다.
    try:
        print("Starting scheduler...")
        scheduler.start()
    except KeyboardInterrupt:
        print("Stopping scheduler...")
        scheduler.shutdown()
        print("Scheduler shut down successfully!")