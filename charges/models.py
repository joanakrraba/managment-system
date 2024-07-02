from django.db import models
from Users.models import User
from task_management.models import Client,Task,Project,Status

class Cost(models.Model):
    name = models.CharField(max_length=225)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.ForeignKey(Client,on_delete=models.CASCADE,related_name='client_costs')
    task = models.ForeignKey(Task,related_name='client_tasks',on_delete=models.SET_NULL,null=True)
    description = models.TextField()
    project = models.ForeignKey(Project,related_name='project_costs',on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=225,choices=Status,default='Requested')
    created_date = models.DateTimeField()
    created_by = models.ForeignKey(User,related_name='user_costs',on_delete=models.SET_NULL,null=True)
    last_modified_date = models.DateTimeField()
    last_modified_by = models.ForeignKey(User,related_name='last_modified_user_costs',on_delete=models.SET_NULL,null=True)

class CostApproval(models.Model):
    name = models.CharField(max_length=225)
    cost = models.ForeignKey(Cost,related_name='cost_approvals',on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=225,choices=Status,default='Draft')
    task = models.ForeignKey(Task,related_name='task_cost_approvals',on_delete=models.SET_NULL,null=True)
    created_date = models.DateTimeField()
    created_by = models.ForeignKey(User,related_name='user_cost_approvals',on_delete=models.SET_NULL,null=True)
    last_modified_date = models.DateTimeField()
    last_modified_by = models.ForeignKey(User, related_name='last_modified_user_cost_approvals',on_delete=models.SET_NULL,null=True)


class Bill(models.Model):
    name = models.CharField(max_length=225)
    client = models.ForeignKey(Client,related_name='client_bills',on_delete=models.CASCADE)
    project = models.ForeignKey(Project,related_name='project_bills',on_delete=models.SET_NULL,null=True)
    description = models.TextField()
    bill_registered_date = models.DateTimeField()
    bill_paid_date = models.DateTimeField()
    total = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=225,choices=Status,default='Draft')
    created_date = models.DateTimeField()

class PaymentRequest(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    bill = models.ForeignKey(Bill,related_name='bill_payment_requests',on_delete=models.CASCADE)
    Cost = models.ForeignKey(Cost,related_name='cost_payment_requests',on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=225,choices=Status,default='Draft')
    created_date = models.DateTimeField()

class Payment(models.Model):
    name = models.CharField(max_length=225)
    cost = models.ForeignKey(Cost,related_name='cost_payments',on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill,related_name='bill_payments',on_delete=models.CASCADE)
    client = models.ForeignKey(Client,related_name='client_payments',on_delete=models.CASCADE)
    project = models.ForeignKey(Project,related_name='project_payments',on_delete=models.SET_NULL,null=True)
    task = models.ForeignKey(Task,related_name='task_payments',on_delete=models.SET_NULL,null=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    created_date = models.DateTimeField()
