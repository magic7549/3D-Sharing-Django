from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    path('', views.index, name='index'),
    path('password/', views.change_password, name='change_password'),
    path('delete/', views.delete, name='delete'),
    path('modeling/', views.my_modeling, name='modeling'),
    path('community/', views.my_community, name='community'),
]