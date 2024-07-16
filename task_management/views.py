from django.shortcuts import render
from django.shortcuts import redirect
from .forms import (TaskForm, ClientForm, ProjectForm, AttachmentForm, IndustryForm,EditTaskForm,EditAttachmentForm,EditIndustryForm,EditClientForm,EditProjectForm)
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
            return redirect('task_management:industry_list')
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

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})

def edit_attachment(request, attachment_id):
    attachment = get_object_or_404(Attachment, id=attachment_id)
    if request.method == 'POST':
        form = EditAttachmentForm(request.POST, instance=attachment_list)
        if form.is_valid():
            form.save()
            return redirect('attachment_list')
    else:
        form = AttachmentForm(instance=attachment)
    return render(request, 'edit_attachment.html', {'form': form})


def edit_industry(request, industry_id):
    industry = get_object_or_404(Industry, id=industry_id)
    if request.method == 'POST':
        form = EditIndustryForm(request.POST, instance=industry_list)
        if form.is_valid():
            form.save()
            return redirect('industry_list')
    else:
        form = IndustryForm(instance=industry)
    return render(request, 'edit_industry.html', {'form': form})

def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = EditClientForm(request.POST, instance=client_list)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'edit_client.html', {'form': form})

def edit_project(request, project_id):
    project = get_object_or_404(Client, id=project_id)
    if request.method == 'POST':
        form = EditProjectForm(request.POST, instance=project_list)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form})









