"""
URL configuration for website project.

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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.todo, name ="todo"),
    path('logout/', views.logout, name = 'logout'),

    path('sign-up/', views.sign_up, name = 'sign_up'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('calender/<int:year_i>/<int:month_i>/<int:day_i>/', views.old_day, name='old_day'),
    path('calendar/', views.calendar, name='calendar'),
    path('customize/', views.week_custom, name='week_custom'),
    path('customize/<int:day_id>/', views.add_default_task, name='add_default_task'),


]
