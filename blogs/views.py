from django.shortcuts import render

# Home page view
def home(request):
    return render(request, 'home.html')

# Barber page view
def barber_home(request):
    return render(request, 'barbers.html')

def practice_view(request):
    
    return render(request, 'practice.html')

def learning_view(request):
    return render(request,'learning.html')
def webpage(request):
    return render(request,'webpage.html')

def webpage2(request):
    return render(request,'webpage2.html')

def webpage3(request):
    return render(request,'webpage3.html')

def praveen_hair_salon(request):
    return render(request,'praveen_hair_salon.html')

def services(request):
    return render(request, 'services.html')

def gallery(request):
    return render(request, 'gallery.html')

def booking(request):
    return render(request, 'booking.html')

def contact(request):
    return render(request, 'contact.html')