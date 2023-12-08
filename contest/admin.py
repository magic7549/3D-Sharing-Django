from django.contrib import admin
from .models import ContestRoundInfo, Contest, PreviousContest

# Register your models here.
admin.site.register(ContestRoundInfo)
admin.site.register(Contest)
admin.site.register(PreviousContest)