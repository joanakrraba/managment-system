

from django.urls import path
from .import views

app_name = 'charges'


urlpatterns = [

    path('payment_list/', views.payment_list, name='payment_list'),
    path('payment_request/',views.payment_request, name='payment_request'),
    path('cost/', views.cost, name='cost'),
    path('cost_approval/', views.cost_approval, name='cost_approval'),
    path('bill/', views.bill, name='bill'),
    path('create_bill/', views.create_bill, name='create_bill'),
    path('create_cost_approval/', views.create_cost_approval, name='create_cost_approval'),
    path('create_cost/', views.create_cost, name='create_cost'),
    path('create_payment_request/', views.create_payment_request, name='create_payment_request'),
    path('create_payment/', views.create_payment, name='create_payment'),
    path('edit_bill/<int:bill_id>/', views.edit_bill, name='edit_bill'),
    path('edit_cost/<int:cost_id>/', views.edit_cost, name='edit_cost'),
    path('edit_cost_approval/<int:cost_approval_id>/', views.edit_cost_approval, name='edit_cost_approval'),
    path('edit_payment_request/<int:payment_request_id>/', views.edit_payment_request, name='edit_payment_request'),
    path('edit_payment/<int:payment_id>/', views.edit_payment, name='edit_payment'),
    path('manage_cost_approval/<int:cost_approval_id>/', views.manage_cost_approval, name='manage_cost_approval'),
    path('update_cost_approval_status/<int:cost_approval_id>/', views.update_cost_approval_status,name='update_status'),
]