from django.shortcuts import render
from django.shortcuts import redirect
from .forms import TaskForm, ClientForm, ProjectForm, AttachmentForm, IndustryForm
from django.shortcuts import get_object_or_404
from task_management.models import *

def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task_list.html',context)

def client_list(request):
    client = Client.objects.all()
    context = {'clients': client}
    return render(request, 'client_list.html',context)


def project_list(request):
    project = Project.objects.all()
    context = {'projects': project}
    return render(request, 'project_list.html', context)

def attachment_list(request):
    attachment = Attachment.objects.all()
    context = {'attachments': attachment}
    return render(request, 'attachment_list.html', context)

def industry_list(request):
    industries = Industry.objects.all()
    context = {'industries': industries}
    return render(request, 'industry_list.html', context)

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()

    return render(request, 'create_client.html', {'form': form})

def create_project (request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})

def create_attachment (request):
    if request.method == 'POST':
        form = AttachmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attachment_list')
    else:
        form = AttachmentForm()
    return render(request, 'create_attachment.html', {'form': form})
def create_industry (request):
    if request.method == 'POST':
        form = IndustryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('industry_list')
    else:
        form = IndustryForm()
    return render(request, 'create_industry.html', {'form': form})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form': form})

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form': form})









