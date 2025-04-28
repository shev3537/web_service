"""
URL configuration for video_streaming project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from videos import views
# # from .views import register
# from django.contrib.auth import views as auth_views
# from videos.views import home
# from videos.views import register 

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('upload/', views.upload_video, name='upload_video'),
#     path('videos/', views.video_list, name='video_list'),
#     path('register/', register, name='register'),
#     path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     path('', home, name='home'),
# ]



from django.contrib import admin
from django.urls import path
from videos import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from videos.views import video_list, add_comment, delete_video

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('upload/', views.upload_video, name='upload_video'),
#     path('videos/', views.video_list, name='video_list'),
#     path('register/', views.register, name='register'),
#     path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     path('', views.home, name='home'),
# ]
urlpatterns = [
    path('upload/', views.upload_video, name='upload_video'),
    path('', views.video_list, name='video_list'),  # Доступно как 'videos:video_list'
    path('register/', views.register, name='register'),
    path('login_view/', views.login_view, name='login_view'),
    path('home', views.home, name='home'),  # Убедитесь, что у вас есть представление для home
    path('video/delete/<int:video_id>/', views.delete_video, name='delete_video'),
    path('add_comment/<int:video_id>/', add_comment, name='add_comment'),
    path('logout/', views.logout_view, name='logout'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



