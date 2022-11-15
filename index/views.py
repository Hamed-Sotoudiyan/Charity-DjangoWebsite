from django.shortcuts import render
import requests
import json
from News.models import news
from videos.models import video
import urllib
from Supporters.models import financialsAids,supporters


# Create your views here.
def home(request):
    news_From_DB = []
    last_index= len(news.objects.all()) - 1
    news_From_DB.append(news.objects.all()[last_index])
    last_index = last_index -1
    news_From_DB.append(news.objects.all()[last_index])
    last_index = last_index -1
    news_From_DB.append(news.objects.all()[last_index])

    last_video = video.objects.all().last()

    last_financialsAids = financialsAids.objects.all().order_by('-id')[:3]

    context ={
        'news_' : [
            {
                'title' : news_From_DB[2].title,
                'image' : urllib.parse.urljoin(urllib.parse.quote('static/img/news/'), news_From_DB[2].image.url),
                'date' : news_From_DB[2].date,
                'text' : news_From_DB[2].text,
            },
            {
                'title' : news_From_DB[1].title,
                'image' : urllib.parse.urljoin(urllib.parse.quote('static/img/news/'), news_From_DB[1].image.url),
                'date' : news_From_DB[1].date,
                'text' : news_From_DB[1].text,
            },
            {
                'title' : news_From_DB[0].title,
                'image' : urllib.parse.urljoin(urllib.parse.quote('static/img/news/'), news_From_DB[0].image.url),
                'date' : news_From_DB[0].date,
                'text' : news_From_DB[0].text,
            },
        ],
        'last_video_for_template' : {
            'lecturer_name' : last_video.lecturer_name,
            'subject' : last_video.subject,
            'description' : last_video.description,
            'video_url' : last_video.video_url,
        },
        'last_financialsAids_forTemplate' : last_financialsAids
    }


    # video image --> style.css --> video_bg_1
    return render(request, 'index/index.html',context)
