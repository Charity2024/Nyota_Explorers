from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
# This view renders a simple welcome message for the home page.