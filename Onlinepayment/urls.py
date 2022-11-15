from django.urls import path
from . import views

app_name = 'Onlinepayment'

urlpatterns = [
    path('', views.main, name='main'),
]
