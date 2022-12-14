from django.shortcuts import render
from .models import Animal

def home(request):
    animals = Animal.objects.all()
    
    context = {
        'animals': animals,
    }
    return render(request, "index.html", context)