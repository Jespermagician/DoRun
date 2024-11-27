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
from hashlib import sha256
from django.shortcuts import get_object_or_404

# The base dorun folder
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

def indexMail(request):
    return HttpResponse("Hello... ")


def generateToken():
    testmail = "test@test.de"
    testsalt = sha256("ghjsdflqkjsgbfjkds".encode('utf-8')).hexdigest()
    print("testsalt")
    print(testsalt)
    token = sha256((testmail + testsalt).encode('utf-8')).hexdigest()
    print("token")
    print(token)
    return token

def UserAuth(request, name: str):
    # Funktion zur Generierung einer eindeutigen ID
    def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    # Pfad zur Datei (Django-Template)
    template_name = "UserAuth.html"
    # template_name = os.path.join(BASE_DIR, "Backend", "CustomData", "UserAuth.html")


    # print("request.get_full_path()")
    # print(request.get_full_path())
    testUserID = 123423
    token = generateToken()
    print("request.build_absolute_uri ")
    print(request.build_absolute_uri())
    
    # target_link = f"{request.build_absolute_uri()}auth/{token}"
    target_link = f"{request.build_absolute_uri()}auth/{testUserID}/{token}"

    print(target_link)


    try:
        # Kontext mit Daten erstellen
        context = {
            'name': name,
            'link_url': target_link
            # 'link_url': f'http://localhost:9000/auth/{id_generator()}'
        }

        # HTML-String aus Template rendern
        # django_engine = engines["django"]
        print(template_name)
        rendered_html = render_to_string(template_name=template_name, context=context, request=request)
        # Ergebnis zurückgeben
        return rendered_html

    except FileNotFoundError:
        print(f"Die Datei '{template_name}' wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return None




def verify_user(request, UserID, token):
    # Suche nach einem Eintrag mit dem Token in der Datenbank
    # user = get_object_or_404(User, id=user_id)

    testsalt = "ghjsdflqkjsgbfjkds"
    testmail = "test@test.de"
    # Token neu generieren
    # generated_token = generate_token(user.email, user.id)
    ComparedToken = generateToken()
    print("--------------------------------------------------")
    print("--------------------------COMPARE-----------------")
    print("--------------------------------------------------")
    print("token 1: ", token)
    print("token new 1: ", ComparedToken)
    print("UserID: ", UserID)



    # Token vergleichen
    if ComparedToken == token:
        # user.is_verified = True  # Verifiziere den Benutzer
        # user.save()  # Änderungen speichern
        print("erfolgreich eigentlich")
        return HttpResponse("Benutzer erfolgreich verifiziert!")
    else:
        return HttpResponse("Ungültiger Token oder Benutzer nicht gefunden.", status=400)