
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('client_list/', views.client_list, name='client_list'),
    path('project_list/', views.project_list, name='project_list'),
    path('create_client/', views.create_client, name='create_client'),
    path('create_project/', views.create_project, name='create_project'),
    path('task/', views.task, name='task'),
    path('task/create/', views.task_create, name='create_task'),
    path('task/update/<int:task_id>/', views.update_task, name='update_task'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
