from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='newuser'

urlpatterns = [
        path('', views.MainView.as_view(), name='all'),
        path('user/create', views.NewuserCreateView.as_view(), name='newuser_create'),
]