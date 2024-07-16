
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
    path('attachment_list/', views.attachment_list, name='attachment_list'),
    path('industry_list/', views.industry_list, name='industry_list'),
    path('create_attachment/', views.create_attachment, name='create_attachment'),
    path('create_industry/', views.create_industry, name='create_industry'),
    path('edit_task', views.edit_task, name='edit_task'),
    path('edit_attachment', views.edit_attachment, name='edit_attachment'),
    path('edit_industry', views.edit_industry, name='edit_industry'),
    path('edit_client', views.edit_client, name='edit_client'),
    path('edit_project', views.edit_project, name='edit_project')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
