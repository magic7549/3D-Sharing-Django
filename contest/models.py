from django.db import models
from django.contrib.auth.models import User
from modeling.models import Modeling


class ContestRoundInfo(models.Model):
    round_num = models.IntegerField(primary_key=True)
    start_date = models.DateField()
    vote_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Round Number : {self.round_num}" 


class Contest(models.Model):
    round_info = models.ForeignKey(ContestRoundInfo, on_delete=models.CASCADE)
    modeling = models.ForeignKey(Modeling, on_delete=models.CASCADE)
    voter = models.ManyToManyField(User, null=True, blank=True)

    def __str__(self):
        return f"Round Number : {self.round_info.round_num}, Model Title : {self.modeling.title}" 


class PreviousContest(models.Model):
    contest_info = models.ForeignKey(Contest, on_delete=models.CASCADE)

    def __str__(self):
        return f"Round Number : {self.contest_info.round_info.round_num}, Model Title : {self.contest_info.modeling.title}" 