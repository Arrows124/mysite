from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('portfolio/', views.WorkView.as_view(), name='portfolio'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]