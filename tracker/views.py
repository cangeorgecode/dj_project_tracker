from django.shortcuts import render, redirect
import datetime
from .models import Project
from django.db.models import Sum
from .forms import ProjectForm
from django.contrib import messages
# from django import forms
import time
from django.contrib.auth import authenticate, login, logout

# List all projects but only allow admin to edit
def index(request):
    cur_year = datetime.datetime.now().strftime("%Y")
    projects = Project.objects.all()
    completed = Project.objects.filter(status=True).count()
    total = Project.objects.count()
    progress = completed/total*100
    progress = round(progress, 2)
    form = ProjectForm()
    context = {
        'cur_year': cur_year,
        'projects': projects,
        'completed': completed,
        'total': total,
        'progress': progress,
        'form': form,
    }
    if request.method == "POST":
        form = ProjectForm(request.POST)
        form.save()
        messages.success(request, "New idea added! Exciting!")
        return redirect('index')

    return render(request, 'tracker/index.html', context)

def viewproject(request, project_id):
    project = Project.objects.get(pk=project_id)
    form = ProjectForm(instance=project)
    context = {
        'project': project,
        'form': form,
    }
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        form.save()
        messages.success(request, 'Project has been updated')
        return redirect('index')
    return render(request, 'tracker/viewproject.html', context)

def delproject(request, project_id):
    project = Project.objects.get(pk=project_id)
    project.delete()
    messages.success(request, 'Project has been deleted')
    return redirect('index')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ('error logging in'))
            return redirect('login')
    return render(request, 'registration/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'bye')
    return redirect('index')