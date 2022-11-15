from django.urls import path
from . import views

app_name = 'adminpage'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.adminpagemenu, name='adminpagemenu'),
    path('adminnews', views.adminnews, name='adminnews'),
    path('adminvideo', views.adminvideo, name='adminvideo'),
    path('admincontacts', views.admincontacts, name='admincontacts'),
    path('adminsupporters', views.adminsupporters, name='adminsupporters'),
    path('adminfinancialsAids', views.adminfinancialsAids, name='adminfinancialsAids'),
    path('adminNonCashAssistance', views.adminNonCashAssistance, name='adminNonCashAssistance'),
]
