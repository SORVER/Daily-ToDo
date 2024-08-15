from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.views import LoginView
from .forms import EmailAuthenticationForm , RegisterForm , DefaultTaskForm
from django.contrib.auth import login as auth_login , logout as auth_logout, authenticate
from .forms import TaskForm , DefaultTask, DefaultDay
from django.shortcuts import get_object_or_404, render, redirect
from datetime import date, timedelta
from .models import *
import calendar

def todo(request):

   form = TaskForm()

   
   if request.method == "POST":

      form = TaskForm(request.POST)

      if form.is_valid():

         default_list, created = Day.objects.get_or_create(date=date.today(), user = request.user)
         task = form.save(commit=False)
         task.day = default_list
         form.save()
      return redirect('/')
   
   list_today, created = Day.objects.get_or_create(date=date.today(), user = request.user)
   if created:
       list_today.save()

   tasks = Task.objects.filter(day = list_today)

   context = {'tasks':tasks, 'form': form}

   return render(request, 'main/todo.html',context)





def sign_up(request):

   if request.method == 'POST':
      form = RegisterForm(request.POST)
      if form.is_valid():
         user = form.save()
         auth_login(request, user)
         return redirect('/')
   else :
      form = RegisterForm()
  
   return render(request, 'registration/sign_up.html', {"form": form})


def logout(request):
   auth_logout(request)
   return redirect('/login/')

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, day__user = request.user)
    #task.completed = not task.completed
    if request.method == "POST":
        task.completed = not task.completed
        task.save()

    return redirect('/')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, day__user = request.user)
    #task.completed = not task.completed
    if request.method == "POST":
        task.delete()
        
    return redirect('/')

def old_day(request, year_i, month_i, day_i):
   our_day = date(year = year_i,month =  month_i,day = day_i)
   list_today =  get_object_or_404( Day, date=our_day, user = request.user)
   tasks = Task.objects.filter(day = list_today)
   return render(request, 'main/old_day.html',{"tasks": tasks, "day": our_day})

def calendar(request):
   return render(request, 'main/calendar.html')

def week_custom(request):
    
    form = DefaultTaskForm()

    return render(request, 'main/customize.html', {"form": form})



def add_default_task(request, day_id):
    
    return render(request, 'main/customize.html')


class CustomLoginView(LoginView):
   authentication_form = EmailAuthenticationForm
   template_name = 'registration/login.html' 

