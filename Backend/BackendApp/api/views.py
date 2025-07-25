#Python default
import json
# from Backend.BackendApp.mail import mail_handle
from mail  import mail_handle
from mail.views import generateToken
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
from .password import pwd # pwd.CheckPassword, Generate_secure_password, PasswordHashing, convertSaltAndHash
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.http import JsonResponse  # Importiere JsonResponse
from django.http import HttpResponse  # Importiere HttpResponse
from django.db.models import Max

from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta

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
        domain = data.get("domain")

        # try:
        #Erstelle neuen Benutzer auf der Datenbank
            # Send Verification Mail

        print("first_name,last_name,email,password")
        print(first_name,last_name,email,password)
        NewUser = Users.RegisterUser(first_name, last_name, email,password)
        # Check if the User is created
        if NewUser == None:
            print("Process interupted. Try Again!")
            # return HttpResponse(content="User couldn't be created!", status=200)
            return JsonResponse(data={}, status=400)
        
        
        mail_handle.sendUserVerifyMail(request=request, UserID=int(NewUser.iduser), frontendDomain=domain)
        # except : 
        # #Bei Fehler return error an Frontend
        #     print("Error occured: ")
            # return JsonResponse(data={"userid": None, "UserIsAuth": False,'message': 'Registrierung nicht erfolgreich'}, status=401)
        
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
        status = 200
        

        # Versuche den Benutzer anzumelden
        user = Users.LoginUser(username,password)
        # -99 = no pwd
        # -100 = to many dries
        # -101 = another error
        
        #Controlls messages
        try:
            if (user.verified == False):
                status = 400
                message = "Der User ist noch nicht verifiziert! Bitte überprüfen Sie Ihre E-Mails. Oder ändern Sie Ihr Passwort!"
            elif (user.verified == True):
                message = "Login erfolgreich"
            else:
                message = "Login nicht erfolgreich"
        except:
            print("user")
            print(user)
            if (user == -99):
                return JsonResponse(status=200, data={"userid": -99,"UserIsAuth": False, 'message': 'Login nicht erfolgreich', "Role": False})
            elif (user == -100):
                status=400
                message = "Zu viele Fehlversuche. Benutzer wurde gesperrt! Passwort zurücksetzen!"
                return JsonResponse({'message': message}, status=401)
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
            return JsonResponse(data=User_Data, status=status)   # Nach erfolgreichem Login weiterleiten (zu einer Seite namens "home")
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
    
# This is a addutional funtion, to get the user with the user-id and to just change the pwd not the salt
@csrf_protect
def resetUserPasswort(request):
    json_data = json.loads(request.body)
    iduser_str = json_data["iduser"]
    oldPwd_entry = json_data["oldPwd"]  
    newPwd = json_data["newPwd"]  
    iduser = int(iduser_str)

    try:
        user = Users.objects.all().get(iduser=iduser)
        if pwd.CheckPassword(EnteredPwd=oldPwd_entry, salt=user.salt, password=user.password_hash) == False:
            return JsonResponse(status=401, data={"message":"Das alte Passwort ist falsch!"})
        Status, Message = Users.SetJustPasswordWith_iduser(iduser, newPwd)
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
    

# bitte nur für das änern von einem eintrag nutzen, was anderers macht auch keinen sinn
@csrf_protect
def UpdateDonations(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)

    try:
        # Parse JSON body into Python list/dict
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=400)

    for entry in data:
        # Extract fields from the entry
        UserID = entry.get("Userid")
        donationid = entry.get("DonoID")
        firstname = entry.get("firstname")
        lastname = entry.get("lastname")
        email = entry.get("email")
        street = entry.get("street")
        housenr = entry.get("houseNr")
        Plz = entry.get("Plz")
        DonoAmount = entry.get("DonoAmount")
        FixedAmount = entry.get("FixedAmount")
        frontendDomain = entry.get("frontendDomain")
        isCertReq = entry.get("iscertreq")

        if FixedAmount == "true" or FixedAmount == True:
            FixedAmount = True
        else:
            FixedAmount = False


        donationid = int(donationid)
        # Create a new donation record if no ID was provided
        if (donationid == -1):
            # query = "Select donationrecid From api_donationrecord Where donationrecid = (Select Max(donationrecid) From api_donationrecord)"
            # DonoID = donationrecord.objects.raw(query)
            MaxDoID = donationrecord.objects.aggregate(Max('donationrecid'))['donationrecid__max']

            #Chech if the new user is the first then id = 1 else max id + 1
            donationid = 1
            if MaxDoID != None:
                donationid = MaxDoID + 1

            try:
                newDonRec = donationrecord(donationrecid = int(donationid),
                                              iduser = UserID,
                                              firstname = firstname,
                                              lastname = lastname,
                                              email = email,
                                              street = street,
                                              housenr = housenr,
                                              postcode = Plz,
                                              donation = float(DonoAmount),
                                              fixedamount = bool(FixedAmount),
                                            #   createdat = CreatedAt,
                                              verified = False,
                                              iscertreq = isCertReq)
                # donationrecord.add(newDonRec)
                print("tessdfsdf")
                newDonRec.save()
                print("tessdfsdf")
                Status = 200
                Message = "Neuer Datensatz angelegt"
            except Exception as e:
                return JsonResponse({"message": f"Failed to create record: {str(e)}"}, status=500)
        else:
            # Update existing record
            try:
                donRec = get_object_or_404(donationrecord, donationrecid=int(donationid))

                # Update only if new values are provided, else keep existing ones
                donRec.firstname = firstname or donRec.firstname
                donRec.lastname = lastname or donRec.lastname
                donRec.email = email or donRec.email
                donRec.street = street or donRec.street
                donRec.housenr = housenr or donRec.housenr
                donRec.postcode = Plz or donRec.postcode
                donRec.donation = DonoAmount or donRec.donation
                donRec.fixedamount = FixedAmount if FixedAmount is not None else donRec.fixedamount
                donRec.verified = False  # Mark as unverified after any update
                donRec.iscertreq = isCertReq
                donRec.save()

            except Exception as e:
                return JsonResponse({"message": f"Failed to update record: {str(e)}"}, status=500)
            
        try:
            print("mail sender")
            print(int(UserID))
            print(int(donationid))
            print(frontendDomain)
            mail_handle.sendDonationVerifyMail(request, int(UserID), int(donationid), frontendDomain)
        except:
            return JsonResponse({"message": "Donations updated successfully, but the mail wasnt send"}, status=200)
        return JsonResponse({"message": "Donations updated successfully"}, status=200)

        
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
            Message = "Der SQL-Befehl liefert folgendes zurueck: " + str(e)
        
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
                # raw funktioniert scheinbar nur für select statements
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
        print("donoid löschen:  ", donoid)
        donationrecord.objects.filter(donationrecid=donoid).delete()

    
    return JsonResponse({"message": "Successfully deleted"}, status=200)


@csrf_protect
def get_users(request):
    #  beschränken auf aktive läufer
    users = Users.objects.filter(roleid=3, verified=True)
    userlist = []

    for user in users:
        user_dict = {
            "iduser": user.iduser,
            "firstname": user.firstname,
            "lastname": user.lastname,
            "email": user.email,
            "roleid": user.roleid,
            "verified": user.verified,
            "kilometers": user.kilometers
        }
        userlist.append(user_dict)

    return JsonResponse({"users": userlist})  # safe=True ist Standard

@csrf_protect
def generate_pwd(request):
    # Parse JSON from request body
    json_data = json.loads(request.body)
    iduser = int(json_data["iduser"])  
    token = json_data["token"]
    timeStamp = json_data["timestamp"]

    # Get user by ID
    user = get_object_or_404(Users, iduser=iduser)

    # Convert hexadecimal timestamp to epoch time (milliseconds)
    epoch_time_back = int(timeStamp, 16)
    timestamp_verification = datetime.fromtimestamp(epoch_time_back / 1000)

    # Check if the timestamp is not older than 20 minutes
    if datetime.now() - timestamp_verification > timedelta(minutes=20):
        return JsonResponse({"message": "EXPIRED"}, status=401)

    # Generate token to compare
    compared_token = generateToken(user.salt, pEMail='-'.join(user.email))

    # Compare the provided token with the generated one
    if compared_token == token:
        # If token is valid, proceed with password generation
        if not user.verified:
            user.verified = True

        # Generate new secure password
        new_pwd = pwd.Generate_secure_password(9)
        new_pwd_hash, salt = pwd.PasswordHashing(new_pwd)

        # Store updated hash and salt
        user.salt, user.password_hash = pwd.convertSaltAndHash(salt, new_pwd_hash)
        user.logintrys = 0
        user.save()

        return JsonResponse({"new": new_pwd}, status=200)
    else:
        # Token mismatch ; status has to be 401!
        return JsonResponse({"message": "INVALID"}, status=401)




def csrf_token_view(request):
    return JsonResponse({"csrftoken": get_token(request)})  # Gibt den CSRF-Token als JSON zurück        