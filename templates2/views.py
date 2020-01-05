from django.shortcuts import render
import requests

from game.models import Characters
from game.filters import CharacterFilter

def index(request):
    characters = Characters.objects.all()

    return render(request, 'game/index.html', {'characters':characters})

def search(request):
    character_list = Characters.objects.all()
    character_filter = CharacterFilter(request.GET, queryset=character_list)
    return render(request, 'game/index/character_list.html', {'filter': character_filter})