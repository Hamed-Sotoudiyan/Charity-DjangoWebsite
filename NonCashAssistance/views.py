from django.shortcuts import render
import requests
from .models import NonCashAssistances
from django.contrib import messages



def home(request):
    if request.method == 'POST':
        if( len(request.POST.get('full_name')) !=0 and len(request.POST.get('message')) !=0
            and len(request.POST.get('phone')) !=0 and len(request.POST.get('address')) !=0):
            fullname_from_template = request.POST.get('full_name')
            phone_from_template = request.POST.get('phone')
            address_from_template = request.POST.get('address')
            message_from_template = request.POST.get('message')

            NonCashAssistanceFormData = NonCashAssistances(full_name=fullname_from_template,
                                          phone=phone_from_template,
                                          address=address_from_template,
                                          message=message_from_template)
            NonCashAssistanceFormData.save()
            messages.success(request, 'فرم کمک غیر نقدی حضرتعالی ثبت شد. بسیار ممنونیم')
        else:
            messages.error(request, 'وارد کردن تمامی موارد اجباری است')
    return render(request,'NonCashAssistance/NonCashAssistance.html')
