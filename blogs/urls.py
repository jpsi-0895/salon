from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.salon, name='salon'),
]