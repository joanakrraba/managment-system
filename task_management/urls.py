
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'task_management'


urlpatterns = [
    path('client_list/', views.client_list, name='client_list'),
    path('project_list/', views.project_list, name='project_list'),
    path('task_list/', views.task_list, name='task_list'),
    path('create_client/', views.create_client, name='create_client'),
    path('create_project/', views.create_project, name='create_project'),
    path('create_task/', views.task_create, name='create_task'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
