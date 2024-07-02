from django.shortcuts import render
from task_management.models import *

def client_list(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        context = {'clients': clients}
        return render(request,'clients_list.html')

