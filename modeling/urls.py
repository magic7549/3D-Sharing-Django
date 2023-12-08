from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import base_views, modeling_views, comment_views

app_name = 'modeling'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:modeling_id>/', base_views.detail, name='detail'),

    # modeling_views.py
    path('modeling/create/', modeling_views.modeling_create, name='modeling_create'),
    path('modeling/modify/<int:modeling_id>/', modeling_views.modeling_modify, name='modeling_modify'),
    path('modeling/delete/<int:modeling_id>/', modeling_views.modeling_delete, name='modeling_delete'),
    path('modeling/vote/<int:modeling_id>/', modeling_views.modeling_vote, name='modeling_vote'),

    # comment_views.py
    path('comment/create/<int:modeling_id>/', comment_views.comment_create, name='comment_create'),
    path('comment/modify/<int:comment_id>/', comment_views.comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>/', comment_views.comment_delete, name='comment_delete'),
    path('comment/vote/<int:comment_id>/', comment_views.comment_vote, name='comment_vote'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)