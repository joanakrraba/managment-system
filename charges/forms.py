from django import forms
from .models import Bill,CostApproval,Cost,PaymentRequest,Payment


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['name', 'client',
                  'project','description',
                  'bill_registered_date','bill_paid_date',
                  'total','status','created_date']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'bill_registered_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'bill_paid_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'status':forms.Select(attrs={'class': 'form-control'}),
            'created_date': forms.DateInput(attrs={'class': 'form-control','type':'date'})

        }

    def __init__(self, *args, **kwargs):
        super(BillForm, self).__init__(*args, **kwargs)


class CostApprovalForm(forms.ModelForm):
    class Meta(object):
        model = CostApproval

        fields = ['name','cost',
                  'status','task',
                  'task','created_date',
                  'created_by','last_modified_date','last_modified_by']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'task': forms.Select(attrs={'class': 'form-control'}),
            'created_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
            'last_modified_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'last_modified_by':forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(CostApprovalForm, self).__init__(*args, **kwargs)


class CostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = ['name', 'amount',
                  'client','task',
                  'description','project',
                  'status','created_date','last_modified_by']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'task': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'created_date':forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'last_modify_by': forms.Select(attrs={'class': 'form-control'})

        }
    def __init__(self, *args, **kwargs):
        super(CostForm, self).__init__(*args, **kwargs)


class PaymentRequestForm(forms.ModelForm):
    class Meta:
        model = PaymentRequest
        fields = ['name', 'description',
                  'bill','amount',
                  'status','created_date']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'bill': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'created_date':forms.DateInput(attrs={'class': 'form-control','type':'date'})
            }

    def __init__(self, *args, **kwargs):
        super(PaymentRequestForm, self).__init__(*args, **kwargs)


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['name', 'cost',
                  'bill','client',
                  'project','task','amount']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.Select(attrs={'class': 'form-control'}),
            'bill': forms.Select(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
            'task':forms.DateInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'})
            }

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)


class EditBillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['name', 'client',
                  'project','description',
                  'bill_registered_date','bill_paid_date',
                  'total','status','created_date']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'bill_registered_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'bill_paid_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'status':forms.Select(attrs={'class': 'form-control'}),
            'created_date': forms.DateInput(attrs={'class': 'form-control','type':'date'})

        }

    def __init__(self, *args, **kwargs):
        super(EditBillForm, self).__init__(*args, **kwargs)

class EditCostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = ['name', 'amount',
                  'client','task',
                  'description','project',
                  'status','created_date','last_modified_by']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'task': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'created_date':forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'last_modify_by': forms.Select(attrs={'class': 'form-control'})

        }
    def __init__(self, *args, **kwargs):
        super(EditCostForm, self).__init__(*args, **kwargs)


class EditCostApprovalForm(forms.ModelForm):
    class Meta(object):
        model = CostApproval

        fields = ['name','cost',
                  'status','task',
                  'task','created_date',
                  'created_by','last_modified_date','last_modified_by']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'task': forms.Select(attrs={'class': 'form-control'}),
            'created_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
            'last_modified_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'last_modified_by':forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(EditCostApprovalForm, self).__init__(*args, **kwargs)


class EditPaymentRequestForm(forms.ModelForm):
    class Meta:
        model = PaymentRequest
        fields = ['name', 'description',
                  'bill','amount',
                  'status','created_date']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'bill': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'created_date':forms.DateInput(attrs={'class': 'form-control','type':'date'})
            }

    def __init__(self, *args, **kwargs):
        super(EditPaymentRequestForm, self).__init__(*args, **kwargs)

class EditPaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['name', 'cost',
                  'bill','client',
                  'project','task','amount']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.Select(attrs={'class': 'form-control'}),
            'bill': forms.Select(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
            'task':forms.DateInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'})
            }

    def __init__(self, *args, **kwargs):
        super(EditPaymentForm, self).__init__(*args, **kwargs)