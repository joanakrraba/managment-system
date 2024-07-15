from django.shortcuts import render
from django.shortcuts import redirect
from .forms import BillForm,CostApprovalForm,CostForm,PaymentRequestForm,PaymentForm
from charges.models import *


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
