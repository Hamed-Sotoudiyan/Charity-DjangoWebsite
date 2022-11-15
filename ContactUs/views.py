from django.shortcuts import render
import requests
import json
from .models import contactus
from django.contrib import messages



# Create your views here.
def main(request):
    if request.method == 'POST':
        if( len(request.POST.get('name')) !=0 and len(request.POST.get('message')) !=0):
            fullname_from_template = request.POST.get('name')
            email_from_template = request.POST.get('email')
            subject_from_template = request.POST.get('subject')
            message_from_template = request.POST.get('message')

            ContactUsFormData = contactus(full_name=fullname_from_template,
                                          email=email_from_template,
                                          subject=subject_from_template,
                                          message=message_from_template)
            ContactUsFormData.save()
            messages.success(request, 'پیام شما با موفقیت ثبت شد، متشکریم.')
        else:
            messages.error(request, 'وارد کردن فیلدهای متن پیام و نام و نام خانوادگی اجباری است')
    return render(request, 'ContactUs/contact.html')
