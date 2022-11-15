from django.urls import path
from . import views

app_name = 'Supporters'

urlpatterns = [
    path('', views.main, name='main'),
]
