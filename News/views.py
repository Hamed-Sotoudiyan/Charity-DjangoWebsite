from django.shortcuts import render
import requests
import json
from News.models import news
import urllib



# Create your views here.
def home(request):
    news_From_DB = news.objects.all()
    context ={
        'news_' : [
            {
                'title' : news_From_DB[4].title,
                'image' : urllib.parse.urljoin(urllib.parse.quote('static/img/news/'), news_From_DB[4].image.url),
                'date' : news_From_DB[4].date,
                'text' : news_From_DB[4].text,
            },
            {
                'title' : news_From_DB[3].title,
                'image' : urllib.parse.urljoin(urllib.parse.quote('static/img/news/'), news_From_DB[3].image.url),
                'date' : news_From_DB[3].date,
                'text' : news_From_DB[3].text,
            },
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
    }
    return render(request, 'News/news.html',context)
