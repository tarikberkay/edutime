"""
URL configuration for edutime project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from home import views as home_views
# from user import views as user_views

urlpatterns = [
    path('edutime/', admin.site.urls),
    path('', home_views.home, name='home'),
    path('about/', home_views.about, name='about'),
    path('contact/', home_views.contact, name='contact'),
    path('elements/', home_views.elements, name='elements'),
    path('gallery/', home_views.gallery, name='gallery'),
    path('login/', home_views.login, name='login'),
    path('', include('user.urls')),
    path('news/', home_views.news, name='news'),
    path('staff/', home_views.staff, name='staff'),
    
]
