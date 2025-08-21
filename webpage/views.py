from django.shortcuts import render

# Create your views here.

def home(request):
    """
    Render the home page.
    """
    return render(request, 'home.html')


def about(request):    
    """
    Render the about page.
    """
    return render(request, 'about.html')

def contact(request):
    """
    Render the contact page.
    """
    return render(request, 'contact.html')

def for_page(request):
    """
    Render the 'for' page.
    """
    return render(request, 'for.html')