#Python default
import json
# from Backend.BackendApp.mail import mail_handle
import mail.mail_handle  as mail_handle
from datetime import date

#Django
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.db import connection
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie, csrf_protect
from django.middleware.csrf import get_token


#Rest
from .models import Users, donationrecord
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.http import JsonResponse  # Importiere JsonResponse
from django.http import HttpResponse  # Importiere HttpResponse

# Create ur views here
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

#Handels the registration page
@csrf_protect
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

            print("first_name,last_name,email,password")
            print(first_name,last_name,email,password)
            NewUser = Users.RegisterUser(first_name,last_name,email,password)
            print("test") # debug
            mail_handle.sendUserVerifyMail(request=request, UserID=int(NewUser.iduser))
        except : 
        # #Bei Fehler return error an Frontend
        #     print("Error occured: ")
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
@csrf_protect
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
            elif (user == -100):
                message = "Zu viele Fehlversuche. Benutzer wurde gesperrt!"
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

@csrf_protect
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
    
@csrf_protect   
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
        
@csrf_protect
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
    
@csrf_protect
def UpdateDonations(request):
#Lege Return Werte fest
    Status = 401
    Message = "Unerwarteter Fehler"
    
     # JSON aus dem Request-Body lesen
    try:
        data = json.loads(request.body)  # JSON-Daten in ein Python-Objekt parsen
    except json.JSONDecodeError as e:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    
    # Über die Liste in der JSON-Datenstruktur iterieren
    for entry in data:
        UserID = entry.get("Userid")
        donationid = entry.get("DonoID")
        firstname = entry.get("firstname")
        lastname = entry.get("lastname")
        email = entry.get("email")
        street = entry.get("street")
        housenr = entry.get("HouseNr")
        Plz = entry.get("Plz")
        DonoAmount = entry.get("DonoAmount")
        FixedAmount = entry.get("FixedAmount")

        Dono = donationrecord.objects.raw("Select * From api_donationrecord Where iduser=%s",[donationid])
        for row in Dono:
            DB_data = row
            break

        # Neuer Eintrag
        if (donationid == None):
            #Erstelle neuen Datensatz 
            CreatedAt = date.today()
            
            MaxDoID = donationid.objects.raw("Select Max( donationrecid ) From api_donationrecord")
            MaxDoID += 1
            try:
                donationrecord.objects.create(donationrecid= MaxDoID,
                                              iduser = UserID,
                                              firstname = firstname,
                                              lastname = lastname,
                                              email = email,
                                              street = street,
                                              housenr = housenr,
                                              postcode = Plz,
                                              donation = DonoAmount,
                                              fixedamount = FixedAmount,
                                              createdat = CreatedAt,
                                              verified = False)

                Status = 200
                Message = "Neuer Datensatz angelegt"
            except e:
                Message = e
                break
        else:
            #Eintrag aktualisieren
            if (firstname==None):
                firstname = DB_data.firstname
        
            if (lastname==None):
                lastname = DB_data.lastname
            
            if (email==None):
                email = DB_data.email
        
            if (street==None):
                street = DB_data.street

            if (housenr==None):
                housenr = DB_data.housenr
        
            if (Plz==None):
                Plz = DB_data.postcode

            if (DonoAmount==None):
                DonoAmount = DB_data.donation
        
            if (FixedAmount==None):
                FixedAmount = DB_data.fixedamount
        
            #Schicke E-Mail raus um Spendenbeleg zu verifizieren @Jesper
            #Code goes here    
            verified = DB_data.verified
        
            # SQL-Abfrage
            sql = "UPDATE api_users SET donationredid = %s, iduser= %s, firstname = %s, lastname = %s, email = %s, street = %s, housenr = %s, postcode %s, donation = %s,fixedamount = %s, createdat=%s, verified=%s WHERE iduser = %s"
            # Parameter
            values = [donationid,UserID,firstname,lastname,email,street,housenr,Plz,DonoAmount,FixedAmount,CreatedAt,verified]

            # SQL ausführen
            try:
                with connection.cursor() as cursor:
                    cursor.execute(sql, values)
                Message = "Daten wurden geupdated"
                Status = 200
            except e:
                Message = "Der SQL-Befehl lifert folgendes zurueck: " + str(e)
        
    return JsonResponse({"message": Message}, status=Status)
        
@csrf_protect
def UpdateUsers(request):
    #Lege Return Werte fest
    Status = 401
    Message = "Unerwarteter Fehler"
    
    # JSON aus dem Request-Body lesen
    try:
        data = json.loads(request.body)  # JSON-Daten in ein Python-Objekt parsen
    except json.JSONDecodeError as e:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    
    # Über die Liste in der JSON-Datenstruktur iterieren
    for entry in data:
        iduser = entry.get("Userid")

        firstname = entry.get("firstname")
        lastname = entry.get("lastname")
        email = entry.get("email")
        roleid = entry.get("Roleid")
        verified = entry.get("verified")
        kilometers = entry.get("Kilometer")

        User = Users.objects.raw("Select * From api_users Where iduser=%s",[iduser])
        for row in User:
            DB_data = row
            break

        # Werte prüfen und ggf. von DB verwenden
        if (iduser == None):
            Message = "Kein User gefunden"
            Status = 401
            break

        if (firstname==None):
            firstname = DB_data.firstname
        
        if (lastname==None):
            lastname = DB_data.lastname
            
        if (email==None):
            email = DB_data.email
        
        if (roleid==None):
            roleid = DB_data.roleid

        if (verified==None):
            verified = DB_data.verified
        
        if (kilometers==None):
            kilometers = DB_data.kilometers
        
         # SQL-Abfrage
        sql = "UPDATE api_users SET firstname = %s, lastname = %s, email = %s, roleid = %s, verified = %s, kilometers=%s WHERE iduser = %s"
        # Parameter
        values = [firstname,lastname,email,roleid,verified,kilometers,iduser]

        # SQL ausführen
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, values)
            Status = 200
            Message= "Daten wurden geupdated"
        except e:
            Message = "Der SQL-Befehl lifert folgendes zurueck: " + str(e)
        
    return JsonResponse({"message": Message}, status=Status)

@csrf_protect
def DelUser(request):
    #Lege Return Werte fest
    Status = 401
    Message = "Unerwarteter Fehler"
    
    # JSON aus dem Request-Body lesen
    try:
        data = json.loads(request.body)  # JSON-Daten in ein Python-Objekt parsen
    except json.JSONDecodeError as e:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    
    # Über die Liste in der JSON-Datenstruktur iterieren
    for entry in data:
        iduser = entry.get("Userid")
        email = entry.get("email")

        if (iduser == None):
            iduser = Users.objects.raw("Select iduser From api_users Where email = %s",[email])    

            if (iduser != None):
                Users.objects.raw("Delete From api_users Where iduser = %s", [iduser])
        
@csrf_protect
def DelDonoRec(request):
    #Lege Return Werte fest
    Status = 401
    Message = "Unerwarteter Fehler"
    
    # JSON aus dem Request-Body lesen
    try:
        data = json.loads(request.body)  # JSON-Daten in ein Python-Objekt parsen
    except json.JSONDecodeError as e:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    # Über die Liste in der JSON-Datenstruktur iterieren
    for entry in data:
        donoid = entry.get("donoid")
        
        donationrecord.objects.raw("Delete From api_users Where iduser = %s", [donoid])

def csrf_token_view(request):
    return JsonResponse({"csrftoken": get_token(request)})  # Gibt den CSRF-Token als JSON zurück        