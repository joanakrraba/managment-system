from django.shortcuts import render
from charges.models import Payment, PaymentRequest, Cost, CostApproval, Bill


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

