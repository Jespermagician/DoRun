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
        #Read data
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
             "message": 'Registrierung erfolgreich'
            }
            
        return JsonResponse(data=User_Data, status=200)

#Login user
@csrf_exempt
def cust_login(request):
    # Wenn das Formular über POST gesendet wurde
    if request.method == 'POST':
        # Benutzerdaten aus dem Formular erhalten
        data = json.loads(request.body)
        username = data.get('email')
        password = data.get('password')

        # Versuche den Benutzer anzumelden
        user = Users.LoginUser(username,password)
        
        #Controlls messages
        try:
            if (user.verified == False):
                message = "Der User ist noch nicht verifiziert!"
            elif (user.verified == True):
                message = "Login erfolgreich"
            else:
                message = "Login nicht erfolgreich"
        except:
            if (user == -99):
                return JsonResponse(status=200, data={"userid": -99,"UserIsAuth": False, 'message': 'Login nicht erfolgreich', "Role": False})
            else:
                message = "Unbekannter User"
        
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
    json_data = json.loads(request.body)
    UserID = int(json_data["userid"])  
    
    if (request.method == 'POST' and UserID):
        Data = donationrecord.GetUserStats(UserID)
        
        if (Data != False):
            return JsonResponse(status = 200, data={"entries": Data})
        else:
            return JsonResponse(status=401, data={'message': 'An unexpected error has occurred'})
    else:
        return JsonResponse({'message': 'User ist nicht Authorisiert!'}, status=401)
    
@csrf_exempt    
def resetpassword(request):
    json_data = json.loads(request.body)
    email = json_data["email"]
    Password = json_data["password"]  
    #Convert from string
    try:
        Status, Message = Users.SetPassword(email,Password)
        
        return JsonResponse(status=Status, data={"message":Message})
        
    except:
        Status = 401
        Message = "Error, cant change password!"
        return JsonResponse(status=Status, data={"message":Message})
        
@csrf_exempt
def adminhome(request):
    json_data = json.loads(request.body)
    UserID = json_data["userid"]
    
    if (request.method == 'POST' and UserID):
        Data = donationrecord.GetAdminStats(UserID)
        
        if (Data != False):
            return JsonResponse(status = 200, data={"entries": Data})
        else:
            return JsonResponse(status=401, data={'message': 'An unexpected error has occurred'})
    else:
        return JsonResponse({'message': 'User ist nicht Authorisiert!'}, status=401)