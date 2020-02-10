"""Doers_ADC1_meroSathi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from userprofile import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from questionPlatform import views as ques_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', ques_views.home, name="index"),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('accounts/signup/', views.register, name="signup"),
    path('account/settings', views.profile_settings, name="profile_settings"),
    path('account/settings/edit_profile', views.edit_profile, name="edit_profile"),
    path('download', views.download_profile_image, name="download"),
    path('bug/', views.bug_report, name="bug"),
    path('test/', views.test, name="test"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
