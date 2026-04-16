from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('gallery/', views.gallery),
    path('booking/', views.booking),
    path('about/', views.about),
    path('dashboard/', views.dashboard),
    path('booking/', views.booking),
]