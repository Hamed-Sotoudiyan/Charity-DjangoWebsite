from django.shortcuts import render,redirect
import requests
import json
# Create your views here.


def main(request):
    return render(request, 'About/main.html')
