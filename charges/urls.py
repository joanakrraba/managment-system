

from django.urls import path
from .import views

urlpatterns = [
    path('payment_list/', views.payment_list, name='payment_list'),
    path('payment_request/',views.payment_request, name='payment_request'),
    path('cost/', views.cost, name='cost'),
    path('cost_approval/', views.cost_approval, name='cost_approval'),
    path('bill/', views.bill, name='bill')

]