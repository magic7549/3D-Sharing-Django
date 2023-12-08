from django.urls import path
from .views import base_views

app_name = 'contest'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('register/<int:modeling_id>/', base_views.registerContest, name='registerContest'),
    path('vote/<int:modeling_id>/', base_views.contest_vote, name='contest_vote'),
]