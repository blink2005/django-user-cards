"""
URL configuration for user_cards project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import search_user.views
import authenticate_user.views

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', search_user.views.index),
    path('search/', search_user.views.index),
    path('create/', search_user.views.create_user),
    path('user/<int:id>/', search_user.views.user_info),
    path('delete/<int:id>/', search_user.views.delete_user),
    path('login/', authenticate_user.views.login_user),
    path('logout/', authenticate_user.views.logout_user),
    path('admin/', admin.site.urls),
]
