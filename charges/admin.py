from django.contrib import admin
from .models import Cost, CostApproval, Bill, PaymentRequest, Payment


class CostAdmin(admin.ModelAdmin):
    list_display = ('name','amount',
                    'client','task',
                    'description','project',
                    'status','created_date',
                    'last_modified_by')
admin.site.register(Cost,CostAdmin)
class CostApprovalAdmin(admin.ModelAdmin):
    list_display = ('name','cost',
                    'status','task',
                    'created_date','created_by',
                    'last_modified_date','last_modified_by')
admin.site.register(CostApproval,CostApprovalAdmin)


class BillAdmin(admin.ModelAdmin):
    list_display = ('name','client',
                    'project','description',
                    'bill_registered_date','bill_paid_date',
                    'total','status',
                    'created_date')
admin.site.register(Bill,BillAdmin)

class PaymentRequestAdmin(admin.ModelAdmin):
    list_display = ('name','description',
                    'bill','amount',
                    'status')
admin.site.register(PaymentRequest,PaymentRequestAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name','cost',
                    'bill','client',
                    'project','task',
                    'amount')

admin.site.register(Payment,PaymentAdmin)
