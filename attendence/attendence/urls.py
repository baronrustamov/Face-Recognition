"""attendence URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from faceRecognition import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('/', include('django.contrib.auth.urls')),
    # for login page
    #url(r'^login/$', auth_views.login),
    path('login/', LoginView.as_view(), name='login'),
    #url(r'^login/$', auth_views.LoginView),
    # for logout
    path('logout/', LogoutView.as_view(), name='logout'),
    #url(r'^logout/$', auth_views.logout),
    #url(r'^logout/$', auth_views.LogoutView),
    # for register
    url(r'^register/$', views.register),
    path('faceRecognition/', include('faceRecognition.urls')),
]
