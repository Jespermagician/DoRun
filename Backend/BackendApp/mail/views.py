# from django.shortcuts import render
import string
import random
# from urllib.request import urlopen
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template import engines
from pathlib import Path
import ntpath
import os

# The base dorun folder
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

def indexMail(request):
    return HttpResponse("Hello... ")


def UserAuth(name: str):
    # Funktion zur Generierung einer eindeutigen ID
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    # Pfad zur Datei (Django-Template)
    template_name = "UserAuth.html"
    # template_name = os.path.join(BASE_DIR, "Backend", "CustomData", "UserAuth.html")

    try:
        # Kontext mit Daten erstellen
        context = {
            'name': name,
            'link_url': f'http://localhost:9000/auth/{id_generator()}'
        }

        # HTML-String aus Template rendern
        # django_engine = engines["django"]
        print(template_name)
        rendered_html = render_to_string(template_name, context=context)

        # Ergebnis zurückgeben
        return rendered_html

    except FileNotFoundError:
        print(f"Die Datei '{template_name}' wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return None
