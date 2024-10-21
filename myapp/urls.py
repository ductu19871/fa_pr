# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('main/', views.main_view, name='main'),
    path('otp/', views.otp_view, name='otp'),
]
