from django.shortcuts import render
from django.shortcuts import redirect
from .forms import BillForm,CostApprovalForm,CostForm,PaymentRequestForm,PaymentForm,EditBillForm,EditCostForm,EditCostApprovalForm,EditPaymentRequestForm,EditPaymentForm
from charges.models import *
from django.shortcuts import get_object_or_404


def payment_list(request):
    if request.method == "GET":
        payments = Payment.objects.all()
        context = {'payments': payments}
        return render(request, 'payment_list.html', context)

def payment_request(request):
     if request.method == "GET":
        payment_requests = PaymentRequest.objects.all()
        context = {'payment_requests': payment_requests}
        return render(request, 'payment_request.html', context)

def cost(request):
    if request.method == "GET":
        costs = Cost.objects.all()
        context = {'costs': costs}
        return render(request, 'cost.html', context)

def cost_approval(request):
    if request.method == "GET":
        cost_approvals = CostApproval.objects.all()
        context = {'cost_approvals':cost_approvals}
        return render(request, 'cost_approval.html', context)


def bill (request):
    if request.method == "GET":
        bills = Bill.objects.all()
        context = {'bills': bills}
        return render(request, 'bill.html', context)

def create_bill (request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill')
    else:
        form = BillForm()
    return render(request, 'create_bill.html', {'form': form})

def create_cost_approval (request):
    if request.method == 'POST':
        form = CostApprovalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cost_approval')
    else:
        form = CostApprovalForm()
    return render(request, 'create_cost_approval.html', {'form': form})

def create_cost(request):
    if request.method == 'POST':
        form = CostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cost')
    else:
        form = CostForm()
    return render(request, 'create_cost.html', {'form': form})

def create_payment_request(request):
    if request.method == 'POST':
        form = PaymentRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_request')
    else:
        form = PaymentRequestForm()
    return render(request, 'create_payment_request.html', {'form': form})

def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')
    else:
        form = PaymentForm()
    return render(request, 'create_payment.html', {'form': form})

def edit_bill(request, bill_id):
    bill = get_object_or_404(Client, id=bill_id)
    if request.method == 'POST':
        form = EditBillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect('bill')
    else:
        form = BillForm(instance=bill)
    return render(request, 'edit_bill.html', {'form': form})

def edit_cost(request, cost_id):
    cost = get_object_or_404(Cost, id=cost_id)
    if request.method == 'POST':
        form = EditCostForm(request.POST, instance=cost)
        if form.is_valid():
            form.save()
            return redirect('cost')
    else:
        form = CostForm(instance=cost)
    return render(request, 'edit_cost.html', {'form': form})

def edit_cost_approval(request, cost_approval_id):
    cost_approval = get_object_or_404(CostApproval, id=cost_approval_id)
    if request.method == 'POST':
        form = EditCostApprovalForm(request.POST, instance=cost_approval)
        if form.is_valid():
            form.save()
            return redirect('cost_approval')
    else:
        form = CostApprovalForm(instance=cost_approval)
    return render(request, 'edit_cost_approval.html', {'form': form})

def edit_payment_request(request, payment_request_id):
    payment_request = get_object_or_404(PaymentRequest, id=payment_request_id)
    if request.method == 'POST':
        form = EditPaymentRequestForm(request.POST, instance=payment_request)
        if form.is_valid():
            form.save()
            return redirect('payment_request')
    else:
        form = PaymentRequestForm(instance=payment_request)
    return render(request, 'edit_payment_request.html', {'form': form})

def edit_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    if request.method == 'POST':
        form = EditPaymentForm(request.POST, instance=payment_list)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'edit_payment.html', {'form': form})