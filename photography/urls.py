"""photography URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from users.views import register,profile
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView,PasswordResetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('photon/',include('photon.urls')),
    path('profile/',profile,name='profile'),
    path('register/',register,name='register'),
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='users/logout.html'),name='logout'),

    path('update/',PasswordChangeView.as_view(
        template_name='users/change_password.html',
        success_url = '/photon'), name='change-pass'),

    path('password_reset/',PasswordResetView.as_view(
        template_name='users/password_reset.html',
        ), name='password_reset'),

    path('password_reset/done/',PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html',
        ), name='password_reset_done'),


    path('password_reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confir.html',
        ), name='password_reset_confirm'),

    path('password_reset_complete/',PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html',
        ), name='password_reset_complete'),


    
    


    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
