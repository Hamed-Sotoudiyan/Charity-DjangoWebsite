from django.shortcuts import render,redirect
import requests
from django.contrib import messages
from .models import payment
# Create your views here.

def main(request):
    if request.method == 'POST':
        if( len(request.POST.get('name')) !=0 and len(request.POST.get('amount')) !=0):
            fullname_from_template = request.POST.get('name')
            phone_from_template = request.POST.get('phone')
            amount_from_template = request.POST.get('amount')

            # run kardan api

            # dar soorat moafaghiat : update database
            # PaymentFormData = payment(full_name=fullname_from_template,
            #                               phone=phone_from_template,
            #                               amount=amount_from_template)
            # PaymentFormData.save()

            # dar soorat shekast : payam monaseb b mokhatab
            # messages.error(request, 'وارد کردن فیلدهای نام و نام خانوادگی و مبلغ قابل پرداخت اجباری است')

        else:
            messages.error(request, 'وارد کردن فیلدهای نام و نام خانوادگی و مبلغ قابل پرداخت اجباری است')
    return render(request, 'Onlinepayment/onlinepayment.html')
