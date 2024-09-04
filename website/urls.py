

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

app_name = 'website'


urlpatterns = [
    path('', views.landing_page, name='landing_page')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

