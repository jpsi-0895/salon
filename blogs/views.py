from django.shortcuts import render

# Home page view
def home(request):
    return render(request, 'home.html')

# Salon page view
def salon(request):
    return render(request,'praveen_hair_salon.html')

def services(request):
    return render(request, 'services.html')

def gallery(request):
    return render(request, 'gallery.html')

def booking(request):
    return render(request, 'booking.html')

def contact(request):
    return render(request, 'contact.html')