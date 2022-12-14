from django.shortcuts import render
from django.http import JsonResponse
from .models import Animal

def home(request):
    animals = Animal.objects.all()
    
    context = {
        'animals': animals,
    }
    return render(request, "index.html", context)

def api(request):
    animals = Animal.objects.all().values()
    animals_list = list(animals)
    
    return JsonResponse(animals_list, safe=False)