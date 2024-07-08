from django.shortcuts import render
from task_management.models import *

def task(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task.html',context)



def client_list(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        context = {'clients': clients}
        return render(request,'clients_list.html',context)

def project_list(request):
    if request.method == 'GET':
        project = Project.objects.all()
        context = {'project': project}
        return render(request, 'project_list.html', context)


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Replace with your desired redirect URL
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form': form})







