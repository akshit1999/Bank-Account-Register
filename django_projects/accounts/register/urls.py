from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='register'

urlpatterns = [
        path('', views.LoginHomeView.as_view(), name='all'),

        path('register/<int:pk>/delete/', views.ProfileDeleteView.as_view(), name='profile_delete'),
        path('register/profile/', views.ProfileCreateView.as_view(), name='profile_create'),
        path('register/<int:pk>/detail/', views.ProfileView.as_view(), name='profile_detail'),
        path('register/<int:pk>/update', views.ProfileUpdateView.as_view(), name='profile_update'),

        path('register/create/account', views.AccountCreateView.as_view(), name='account_create'),
        path('register/<int:pk>/delete/account', views.ProfileDeleteView.as_view(), name='account_delete'),
        path('register/<int:pk>/detail/account', views.AccountDetailView.as_view(), name='account_detail'),

        path('register/classify', views.ClassifierOCR.as_view(), name='classifier_ocr'),
]