from django.shortcuts import render,redirect
import requests
import json
from News.models import news
from videos.models import video
from ContactUs.models import contactus
from Supporters.models import supporters,financialsAids
from django.contrib.auth import authenticate,login,logout
from NonCashAssistance.models import NonCashAssistances



# Create your views here.
def home(request):
    if request.method == 'POST':
        username_from_template = request.POST.get('username')
        password_from_template = request.POST.get('password')
        user = authenticate(request,username=username_from_template,password=password_from_template)
        if user is not None:
            login(request,user)
            return redirect('adminpage:adminpagemenu')
    return render(request, 'adminpage/adminlogin.html')

def adminpagemenu(request):
    if request.method == 'POST':
        logout(request)
        return redirect('adminpage:home')
    return render(request, 'adminpage/adminpage.html')

def adminnews(request):
    if request.method == 'POST':
        newstext_from_template = request.POST.get('newstext')
        newstitle_from_template = request.POST.get('newstitle')
        newsdate_from_template = request.POST.get('newsdate')
        newsimage_from_template = request.POST.get('newsimage')

        NewsFormData = news(title=newstitle_from_template,
                                      date=newsdate_from_template,
                                      text=newstext_from_template,
                                      image=newsimage_from_template)
        NewsFormData.save()
    return render(request, 'adminpage/adminnews.html')


def adminvideo(request):
    if request.method == 'POST':
        description_from_template = request.POST.get('description')
        lecturer_name_from_template = request.POST.get('lecturer_name')
        subject_from_template = request.POST.get('subject')
        video_url_from_template = request.POST.get('video_url')
        image_from_template = request.POST.get('image')

        NewsFormData = video(lecturer_name=lecturer_name_from_template,
                                      subject=subject_from_template,
                                      description=description_from_template,
                                      video_url=video_url_from_template,
                                      image=image_from_template)
        NewsFormData.save()
    return render(request, 'adminpage/adminvideo.html')

def admincontacts(request):
    context = {
        'recieved_contacts_for_template' : contactus.objects.all()
    }
    return render(request, 'adminpage/admincontacts.html',context)

def adminsupporters(request):
    context = {
        'registered_supporters_for_template' : supporters.objects.all()
    }

    if request.method == 'POST':
        full_name_from_template = request.POST.get('full_name')
        city_from_template = request.POST.get('city')
        phone_from_template = request.POST.get('phone')
        sms_from_template_TEMP = request.POST.get('sms')
        if sms_from_template_TEMP == 'on':
            sms_from_template = True
        else:
            sms_from_template = False
        NewsFormData = supporters(full_name=full_name_from_template,
                                      city=city_from_template,
                                      phone=phone_from_template,
                                      sms=sms_from_template)
        NewsFormData.save()
    return render(request, 'adminpage/adminsupporters.html',context)

def adminfinancialsAids(request):
    context = {
        'registered_supporters_for_template' : supporters.objects.all(),
        'financialsAids_UntilNow' : financialsAids.objects.all(),
    }
    if request.method == 'POST':

        for row in context['registered_supporters_for_template'] :
            if row.id == int(request.POST.get('supporter')) :
                supporter_from_template = row

        description_from_template = request.POST.get('description')
        NewsFormData = financialsAids(supporter=supporter_from_template,
                                      description=description_from_template)
        NewsFormData.save()
    return render(request, 'adminpage/adminfinancialsAids.html',context)

def adminNonCashAssistance(request):
    context = {
        'NonCashAssistances_for_template' : NonCashAssistances.objects.all(),
    }
    if request.method == 'POST':

        for row in context['NonCashAssistances_for_template'] :
            if row.id == int(request.POST.get('caseid')) :
                caseid_from_template = row

        NonCashAssistances_FormData = NonCashAssistances(action=True)
        NonCashAssistances.objects.filter(id=row.id).update(action=True)
    return render(request,'adminpage/adminNonCashAssistance.html',context)
