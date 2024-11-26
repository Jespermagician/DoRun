from django.shortcuts import render
from django.http import JsonResponse
from .models import Users
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json

# Create ur views here
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

#Handels the registration page
@csrf_exempt
def register(request):
    if request.method == 'POST':
        # Daten auslesen
        data = json.loads(request.body)
        first_name = data.get("firstname")
        last_name = data.get("lastname")
        email = data.get("email")
        password = data.get("password")

        try:
        #Erstelle neuen Benutzer auf der Datenbank
            print(first_name,last_name,email,password)
            NewUser = Users.RegisterUser(first_name,last_name,email,password)

        except: 
        #Bei Fehler return error an Frontend
            return JsonResponse({'message': 'Registrierung nicht erfolgreich'}, status=401)
        
        #Convert Userid
        NewUser = int(NewUser.iduser)
            
        return JsonResponse({'message': 'Registrierung erfolgreich' + str(NewUser)}, status=200)

#Login user
@csrf_exempt
def cust_login(request):
    # Wenn das Formular über POST gesendet wurde
    # return JsonResponse({'message': 'Login erfolgreich'}, status=200)
    if request.method == 'POST':
        # Benutzerdaten aus dem Formular erhalten
        data = json.loads(request.body)
        username = data.get('email')
        password = data.get('password')

        # Versuche den Benutzer anzumelden
        user = Users.LoginUser(username,password)
        userid = user.iduser
        
        if user is not None:
            # Erfolgreiche anmeldung
            # Setzt für die session die anmeldung auf true(Verwendung um Seiten nur für Nutzer anzuzeigen) 
            request.session["UserIsAuth"] = True
            request.session["iduser"] = userid
            messages.success(request, 'Erfolgreich eingeloggt!')
            return JsonResponse({'message': 'Login erfolgreich'}, status=200)   # Nach erfolgreichem Login weiterleiten (zu einer Seite namens "home")
        else:
            # Fehlgeschlagene anmeldung
            # Setzt für die session die anmeldung auf false(Verwendung um Seiten für nicht Nutzer zu blockieren)
            request.session["UserIsAuth"] = False
            messages.error(request, 'Benutzername oder Passwort sind falsch.')
            return JsonResponse({'message': 'Login nicht erfolgreich'}, status=401)  # Benutzer zurück zur Login-Seite leiten

def home(request):
# Prüft ob ein Benutzer angemeldet ist    
    if (request.session["UserIsAuth"] == True):
        return render(request, 'home.html')