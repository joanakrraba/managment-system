from django.db import models
from Users.models import User




Priority_Choices = (
    ("Urgent","Urgent"),
    ("High","High"),
    ("Medium","Medium"),
    ("Low","Low"),
    )

Status = (
    ("Backlog","Backlog"),
    ("In Progress","In Progress"),
    ("In Review","In Review"),
    ("Scheduled","Scheduled"),
    ("Done","Done"),
)
class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    assegnee = models.ForeignKey(User,on_delete=models.SET_NULL,related_name="assegnees",null=True)
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL,related_name="reporters",null=True)
    deadlineDate = models.DateField()
    createdDate = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='tasks_created',on_delete=models.SET_NULL,null=True)
    last_modified_by = models.ForeignKey(User, related_name='tasks_modified',on_delete=models.SET_NULL,null=True,blank=True)



    #Other fields
    priority = models.CharField(max_length=225,choices=Priority_Choices,default="Normal")
    status = models.CharField(max_length=225,choices=Status,default="")


class Attachment(models.Model):
    task = models.ForeignKey(Task,on_delete=models.SET_NULL,related_name='tasks',null=True)
    file = models.FileField(upload_to='attachments/')
    createdDate = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='attachments_created',null=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='attachments_modified',null=True)