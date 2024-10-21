# myapp/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('main/', views.main_view, name='main'),
    path('otp/', views.otp_view, name='otp'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('logout/', views.logout_view, name='logout'),

]
