from django.contrib import admin
from .models import Cost
class CostAdmin(admin.ModelAdmin):
    list_display = ('name','amount',
                    'client','task',
                    'description','project',
                    'status','created_date',
                    'created_by','last_modified_date'
                    'last_modified_by')
admin.site.register(Cost,CostAdmin)
class CostApprovalAdmin(admin.ModelAdmin):
    list_display = ('name','cost',
                    'status','task',
                    'created_date','created_by',
                    'last_modified_date','last_modified_by')
admin.site.register(Cost,CostApprovalAdmin)