
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('charges/',include('charges.urls')),
    path('task_management/',include('task_management.urls')),
    path('',include('website.urls'))
]
