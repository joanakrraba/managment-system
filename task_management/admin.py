from django.contrib import admin
from .models import Task, Project, Attachment,Industry,Client


class TaskAdmin(admin.ModelAdmin):
    list_display = ["title",
                    "assegnee",
                    "reporter",
                    "deadlineDate",
                    "createdDate",
                    "created_by",
                    "last_modified_by"]
admin.site.register(Task,TaskAdmin)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ["task",
                    "file",
                    "createdDate",
                    "created_by",
                    "last_modified_date",
                    "last_modified_by"]

admin.site.register(Attachment,AttachmentAdmin)

class IndustryAdmin(admin.ModelAdmin):
    list_display = ["name","description"]
admin.site.register(Industry,IndustryAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ["name","description",
                    "active","industry",
                    "email","phone",
                    "user"]
admin.site.register(Client,ClientAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["client","name",
                    "status","start_date",
                    "end_date","total_costs"]
admin.site.register(Project,ProjectAdmin)


