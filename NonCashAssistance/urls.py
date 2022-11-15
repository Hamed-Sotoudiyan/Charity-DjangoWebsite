from django.urls import path
from . import views

app_name = 'NonCashAssistance'

urlpatterns = [
    path('', views.home, name='home'),
]
