from django.shortcuts import render
from django.http import HttpResponse

def payment_info(request):
    # Your logic to display or handle payment info goes here
    return HttpResponse("Payment Info Page")