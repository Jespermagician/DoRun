from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
from .models import Users
from django.http import JsonResponse
from .models import Users, donationrecord
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
from mail import interface

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
            # Send Verification Mail
            print(first_name,last_name,email,password)
            NewUser = Users.RegisterUser(first_name,last_name,email,password)
            interface.sendUserVerifyMail(request=request, UserID=int(NewUser.iduser))

        except: 
        #Bei Fehler return error an Frontend
            return JsonResponse(data={"userid": None, "UserIsAuth": False,'message': 'Registrierung nicht erfolgreich'}, status=401)
        
        #Convert Userid
        NewUserID = int(NewUser.iduser)

        
        
        User_Data = {
             "userid": NewUserID,
             "UserIsAuth": False,
             "message": 'Registrierung erfolgreich' + str(NewUserID)
            }
            
        return JsonResponse(data=User_Data, status=200)

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
        print(username,password)
        user = Users.LoginUser(username,password)
        
        #Controlls messages
        if (user.verified == False):
            message = "Der User ist noch nicht verifiziert!"
        elif (user.verified == True):
            message = "Login erfolgreich"
        else:
            message = "Login nicht erfolgreich"
        
        # Get Userid
        try:
            userid = user.iduser
        except:
            User_Data = {
                "userid": None,
                "UserIsAuth": False,
                "message": message,
                "Role": False,
            }
            return JsonResponse(status=401, data={"userid": None,"UserIsAuth": False, 'message': 'Login nicht erfolgreich', "Role": False})
        
        if user is not None:
            # Erfolgreiche anmeldung
            # Setzt für die session die anmeldung auf true(Verwendung um Seiten nur für Nutzer anzuzeigen) 
            
            User_Data = {
                "userid": userid,
                "UserIsAuth": user.verified,
                "message": message,
                "Role": user.roleid,
            }
            messages.success(request, 'Erfolgreich eingeloggt!')
            return JsonResponse(data=User_Data, status=200)   # Nach erfolgreichem Login weiterleiten (zu einer Seite namens "home")
        else:
            # Fehlgeschlagene anmeldung
            # Setzt für die session die anmeldung auf false(Verwendung um Seiten für nicht Nutzer zu blockieren)
            request.session["UserIsAuth"] = False
            messages.error(request, 'Benutzername oder Passwort sind falsch.')
            return JsonResponse({'message': message}, status=401)  # Benutzer zurück zur Login-Seite leiten

@csrf_exempt
def home(request):
# Prüft ob ein Benutzer angemeldet ist    
    if (request.session["UserIsAuth"] == True and request.method == 'POST'):
        
        UserID = request.session["iduser"]
        
        Data = donationrecord.GetUserStats(UserID)
        
        return JsonResponse(Data)
    else:
        return JsonResponse({'message': 'User ist nicht Authorisiert!'}, status=401)