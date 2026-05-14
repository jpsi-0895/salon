from django.urls import path
from . import views

urlpatterns = [
    path('blogs/home/', views.home),
    path('blogs/barbers/', views.barber_home),
    path('blogs/practice/', views.practice_view),
    path('blogs/learning/',views.learning_view),
    path('blogs/webpage/',views.webpage,name='webpage'),
    path('blogs/webpage2/',views.webpage2,name='webpage2'),
    path('blogs/webpage3/',views.webpage3,name='webpage3'),
    path('blogs/prs/',views.praveen_hair_salon,name='praveen_hair_salon'),
    path('blogs/services/', views.services, name='services'),
    path('blogs/gallery/', views.gallery, name='gallery'),
    path('blogs/booking/', views.booking, name='booking'),
    path('blogs/contact/', views.contact, name='contact'),
]