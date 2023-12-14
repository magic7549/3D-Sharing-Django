from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contest/', include('contest.urls')),
    path('modeling/', include('modeling.urls')),
    path('community/', include('community.urls')),
    path('mypage/', include('mypage.urls')),
    path('common/', include('common.urls')),
    path('', views.home, name='home'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)