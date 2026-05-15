from django.shortcuts import render
from .forms import ContactForm

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
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            success = True
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'success': success,
    })