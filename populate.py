import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','mel_cardgame.settings')

import django
django.setup()

import requests

from game.models import Characters

def populate():
    for id in range(1,493):
        url = "https://rickandmortyapi.com/api/character/%s" % (id)

        r = requests.get(url).json()

        character_instance = Characters(
            name= r['name'],
            status= r['status'],
            species= r['species'],
            origin= r['origin']['name'],
            image = r['image'],
        )
        character_instance.save()

populate()












