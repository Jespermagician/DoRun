from django.db import models
from datetime import date
from django.shortcuts import redirect
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import logout
from django.http import JsonResponse
import array
from hashlib import sha256
import random
import string

# Create your models here.
class Users(models.Model):
    iduser = models.IntegerField(primary_key=True, null=False)
    firstname = models.TextField(null=False)
    lastname = models.TextField(null=False)
    email = models.EmailField(unique=False, null=False)
    password_hash = models.BinaryField(null=False)
    salt = models.BinaryField(null=False)
    createdat = models.DateTimeField(auto_now_add=True, null=False)
    roleid = models.IntegerField(null=False)
    kilometers = models.IntegerField(null=False)
    verified = models.BooleanField()
    
    def RegisterUser(first_name,last_name,email,password):
        #1. Set UserID
        #Check if email already exists
        double = False
        try:
            CheckForDoubleUser = Users.objects.raw("Select * From api_users Where email = "+ "'" + email + "'")
            for p in CheckForDoubleUser:
                double = True
        except:
            double = False
        
        try:
            if (double == False):
                #Get current highest iduser
                query = "Select iduser From api_users Where iduser = (Select Max(iduser) From api_users)"
                user = Users.objects.raw(query)

                #Chech if the new user is the first then id = 1 else max id + 1
                for p in user:
                    if (p.iduser != None):
                        UserID = p.iduser
                        UserID = UserID + 1
                    elif (p.iduser == None):
                        UserID = 1
                
        except:
            print("Unexpected error ocurred!")
        
        #2. Password hashing
        if (password != None):
            Password_hash, Salt = PasswordHashing(password)
            
        #3. Set current date 
        CreatedAt = date.today()
        
        #4. Set RoleID = 3 aka User
        RoleID = 3 
        
        #5. Set user-validation validation set by Link to true
        Kilometers = 0
        VerifiedUser = False
        
        #Creat new DB entry if values are filled    
        if (UserID != None and first_name != None and last_name != None and email != None and Password_hash != None and Salt != None and CreatedAt != None and RoleID != None):
            try:
                print("Creating new User with ID: " + str(UserID))
                NewUser = Users.objects.create(
                    iduser=UserID, 
                    firstname=first_name,
                    lastname=last_name,
                    email=email,
                    password_hash=bytearray.fromhex(Password_hash),
                    salt=bytearray.fromhex(Salt),
                    createdat=CreatedAt,
                    roleid=RoleID,
                    verified=VerifiedUser, 
                    kilometers=Kilometers)
            except:
                print("Error, user can't be added to DB")
        else:
            print("Not all requirements are fulfilled to create a user")
        
        return NewUser
 
    # end def

    def LoginUser(email,password):
        #%s is to prevent SQL-injection
        try:
            #Get data to the provided email
            LoginUser = Users.objects.raw("Select * From api_users Where email = %s", [email])
            for p in LoginUser:
                #Init password 
                test = str(b'')
                #If init password eq user password then trigger reset
                if (str(p.password_hash) == test):
                    return -99
                
                # Enter the entered password encrypt it with the salt and compare it with the pwhash from the db
                Password_correct = CheckPassword(password, p.password_hash, p.salt)
                
                if (Password_correct == True):
                    #Return LoginUser
                    return p
        except:
            print("Error")
    
    def SetPassword(email,Password):
        Message = ""
        Status = 401
        try:
            Password_hash, Salt = PasswordHashing(Password)
            Users.objects.filter(email=email).update("password_hash", Password_hash, "salt", Salt )
            Message = "Password changed succesfully"
            Status = 200
        except:
            Message = "Cant set password!"
            
        return Status, Message
    
class donationrecord(models.Model):
    donationrecid = models.IntegerField(primary_key=True, null=False)
    iduser = models.TextField(null=False)
    firstname = models.TextField(null=False)
    lastname = models.TextField(null=False)
    email = models.EmailField(unique=False, null=False)
    street = models.TextField(null=False)
    housenr = models.TextField(null=False)
    postcode = models.TextField(null=False)
    donation = models.FloatField(null=True)
    fixedamount = models.BooleanField(null=True)
    createdat = models.DateTimeField(auto_now_add=True, null=False)
    verified = models.BooleanField(null=True)
    
    def GetUserStats(Userid):
        #Get Userdata for Welcome Screen 
        UserName = Users.objects.raw("Select iduser, firstname, lastname, email From api_users Where iduser = %s", [Userid])
        
        for row in UserName:
            UserFirstname = row.firstname
            UserLastname = row.lastname
            UserEmail = row.email
        
        #Get donationrecord for the loggedin user
        UserEntrys = donationrecord.objects.raw("Select * From api_donationrecord Where iduser = %s", [Userid])
        #Get Userdat 
        UserData = Users.objects.raw("Select * From api_users Where iduser = %s", [Userid])
        
        TotalDonations = 0
        TotalKilometers = 0
        #Get Total amount for Donations and Total Kilomers
        for row in UserData:
            kilometers = row.kilometers
        
        try:
            for row in UserEntrys:
                #Calculate total Donations 
                if (row.fixedamount == True):
                    TotalDonations += row.donation
                else:
                    TotalDonations = TotalDonations + (row.donation * kilometers)
            
                TotalKilometers += kilometers
        except:
            print("Can't calculate without data")
        
        data = []
        #Safe evaluation
        data.append({
            "UserFirstname": UserFirstname,
            "UserLastname": UserLastname,
            "UserEmail": UserEmail,
            "TotalDonations": TotalDonations,
            "TotalKilometers": TotalKilometers})
        
        if (kilometers): 
            # Schleife durch die UserEntrys-Objekte
            for obj in UserEntrys:
                data.append({
                "firstname": obj.firstname,
                "lastname": obj.lastname,
                "email": obj.email,
                "street": obj.street,
                "housenr":obj.housenr,
                "postcode": obj.postcode,
                "donation": obj.donation,
                "fixedamount": obj.fixedamount,
                "createdat": date.today(),
                "verified": obj.verified,
                "Kilometer": kilometers,
                })

        #return JSON 
        return data
    
    def GetAdminStats(Userid):
        #vars
        Message = "Permission denied"
        data = []
        #Get Userdata for welcome screen 
        UserName = Users.objects.raw("Select iduser, firstname, lastname, email From api_users Where iduser = %s", [Userid])
        
        for row in UserName:
            UserFirstname = row.firstname
            UserLastname = row.lastname
            UserEmail = row.email
            Roleid = row.roleid

        if (Roleid < 3):
            Message = "Permission granted"
        
        #Safe evaluation
        data.append({
            "UserFirstname": UserFirstname,
            "UserLastname": UserLastname,
            "UserEmail": UserEmail,
            "Message": Message})


        if (Roleid == 1 or Roleid == 2):
            #Get Userdat 
            UserData = Users.objects.all()
            
            for row in UserData:
            
                data.append({"firstname": row.firstname,
                            "lastname": row.lastname,
                            "email": row.email,
                            "createdat": row.createdat,
                            "verified": row.verified,
                            "kilometers": row.kilometers})
        
        return data
    
    def Create_donationrecord():
        """
        Purpose: Creates a new donationrecord with recived data
        """
        
        data = []
        #Safe evaluation
        #data.append({
        #    "UserFirstname": UserFirstname,
        #    "UserLastname": UserLastname,
        #    "UserEmail": UserEmail
            
        donorec = "Test"
        iduser = "Test"
        f_name = "Test"
        l_name = "Test"
        email = "Test"
        street = "Test"
        housenr = "Test"
        postcode = "Test"
        donation = "Test"
        fixedamount = False
        createdat = date.today()
        verified = False
        
        #Userdaten allgemein
        #Alle daten aus user (firstname, lastname, email, createdat, verified, kilometers)
        
        NewDonoRec = donationrecord.objects.create(donationrecid = donorec, iduser = iduser, firstname = f_name, lastname = l_name, email = email, street = street, housenr = housenr, postcode = postcode, donation = donation, fixedamount = fixedamount, createdat = createdat, verified = verified)
            
    # end def
            
def roles():
    roleid = models.IntegerField(primary_key=True,null=False)
    rolename = models.TextField(null=False)

# Method to create string of random chars
def RandChars(size=30, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def PasswordHashing(password):
    SaltText = RandChars()                                              # Generiert zufällige Zeichenabfolge   
    Salt = sha256(SaltText.encode('utf-8')).digest().hex()              # Erstellt den Hash des Salts
    Password_Hash = sha256((password + Salt).encode('utf-8')).digest()  # Verschlüsselung des Passwords und Salt
    return Password_Hash.hex(), Salt                                    # Rückgabe

def CheckPassword(EnteredPwd, password, salt):                          
    EnteredPwdHash = sha256((EnteredPwd + salt.hex()).encode('utf-8')).digest() # Bildet den Hash nach
    is_valid = EnteredPwdHash == password                                       # Vergleicht den Gespeicherten und Neu generierten Hash
    return is_valid                                                             # Gibt einen Boolschen Wert zurück

class CustomBackend(BaseBackend):
    def get_user(self, user_id):
        return Users(id=user_id, username='benutzername')

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡈⠛⢉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⢿⣿⣿⣿⣿⣿⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⢰⣿⡏⠀⢸⣿⣿⣿⣿⡇⢸⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⣼⣿⠁⠀⢸⣿⣿⣿⣿⠁⠀⠙⠻⢿⣿⣶⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠛⠋⠀⠀⠸⣿⣿⣿⡏⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠙⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣦⠈⢿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡟⠀⠀⠻⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⠁⠀⠀⠀⠘⢿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⢾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠈⢻⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀