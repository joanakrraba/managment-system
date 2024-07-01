from django.db import models
from Users.models import User
from task_management.models import Client,Task,Project,Status

class Cost(models.Model):
    name = models.CharField(max_length=225)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.ForeignKey(Client,on_delete=models.CASCADE,related_name='client_costs')
    task = models.ForeignKey(Task,related_name='client_tasks',on_delete=models.CASCADE)
    description = models.TextField()
    project = models.ForeignKey(Project,related_name='project_costs',on_delete=models.CASCADE)
    status = models.CharField(max_length=225,choices=Status,default='Requested')
    created_date = models.DateTimeField()
    created_by = models.ForeignKey(User,related_name='user_costs',on_delete=models.CASCADE)
    last_modified_date = models.DateTimeField()
    last_modified_by = models.ForeignKey(User,related_name='last_modified_user_costs',on_delete=models.CASCADE)

class CostApproval(models.Model):
    name = models.CharField(max_length=225)
    cost = models.ForeignKey(Cost,related_name='cost_approvals',on_delete=models.CASCADE)
    status = models.CharField(max_length=225,choices=Status,default='Draft')
    task = models.ForeignKey(Task,related_name='task_cost_approvals',on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    created_by = models.ForeignKey(User,related_name='user_cost_approvals',on_delete=models.CASCADE)
    last_modified_date = models.DateTimeField()
    last_modified_by = models.ForeignKey(User, related_name='last_modified_user_cost_approvals',on_delete=models.CASCADE)
