from django.db import models
from datetime import date
from django.shortcuts import redirect
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import logout
from django.http import JsonResponse
import array
from django.db import connection
from hashlib import sha256
import random
import string
import re

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
    logintrys = models.IntegerField(default=0)
    
    def RegisterUser(first_name,last_name,email,password):

        # Password validation
        validation = checkPwdConstraints(password)
        if (validation != 1):
            print("Password is not valid")
            return None
        
        #1. Set UserID
        #Check if email already exists
        double = False
        UserID = None
        try:
            CheckForDoubleUser = Users.objects.raw("Select * From api_users Where email = "+ "'" + email + "'")
            for p in CheckForDoubleUser:
                double = True
        except:
            double = False
        print("double " + str(double))
        try:
            if (double == False):
                #Get current highest iduser
                query = "Select iduser From api_users Where iduser = (Select Max(iduser) From api_users)"
                user = Users.objects.raw(query)

                #Chech if the new user is the first then id = 1 else max id + 1
                test = False
                for p in user:
                    test = True
                    if (p.iduser != None):
                        UserID = p.iduser
                        UserID = UserID + 1
                    elif (p.iduser == None):
                        UserID = 1
                print("test " + str(test))
                
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
        
        NewUser = None
        #Creat new DB entry if values are filled    
        print("UserID")
        print(UserID)
        if (UserID != None and first_name != None and last_name != None and email != None and Password_hash != None and Salt != None and CreatedAt != None and RoleID != None):
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
            return NewUser
            # try:
            # except:
            #     print("Error, user can't be added to DB!")
        else:
            print("Not all requirements are fulfilled to create a user")
        
        # if the process was denied, no NewUser is created
        return None
 
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
                    print(p.password_hash, test)
                    print("No password for User")
                    return -101
                
                # Enter the entered password encrypt it with the salt and compare it with the pwhash from the db
                Password_correct = CheckPassword(password, p.password_hash, p.salt)
                
                logintrys = p.logintrys

                if (Password_correct == True):
                    #Return LoginUser
                    
                    if (logintrys <= 5):
                        logintrys = 0
                        sql = "UPDATE api_users SET logintrys = %s WHERE email = %s"
                        # Parameter
                        values = [logintrys,email]

                        # SQL ausführen
                        try:
                            with connection.cursor() as cursor:
                                cursor.execute(sql, values)
                        except:
                            return -101
                        return p
                    else:
                        return -100
                    
                else:
                    logintrys = logintrys + 1
                    sql = "UPDATE api_users SET logintrys = %s WHERE email = %s"
                    # Parameter
                    values = [logintrys,email]
                    
                    # SQL ausführen
                    try:
                        with connection.cursor() as cursor:
                            cursor.execute(sql, values)
                        if (logintrys > 5):
                            return -100
                        return -101
                    except:
                        return -101
                    
        except:
            print("Error")
    
    def SetPassword(email,Password):
        Message = ""
        Status = 401
        try:
            Password_hash, Salt = PasswordHashing(Password)
            print(Password_hash, Salt)
            
            # SQL-Abfrage
            sql = "UPDATE api_users SET password_hash = %s, salt = %s WHERE email = %s"
            # Parameter
            values = [bytearray.fromhex(Password_hash), bytearray.fromhex(Salt), email]

            # SQL ausführen
            with connection.cursor() as cursor:
                cursor.execute(sql, values)
                
            Message = "Password changed succesfully"
            Status = 200
        except:
            Message = "Cant set password!"
            
        return Status, Message

    def SetJustPasswordWith_iduser(iduser,Password):
        Message = ""
        Status = 401
    
        match checkPwdConstraints(Password):
            case -1:
                Message = "Password muss ein Buchstaben, eine Zahl und ein Sonderzeichen enthalten!"
                Status = 401
                return Status, Message
            case 0:
                Message = "Password muss mindestens 8 Zeichen lang sein!"
                Status = 401
                return Status, Message
        print("Password is valid")
        try:
            salt = Users.objects.get(iduser=iduser).salt
            print("salt: ", salt)
            Password_hash = PasswordSetJustPassword(password=Password, salt=salt)

            print("Password_hash: ", Password_hash)
            # SQL-Abfrage
            sql = "UPDATE api_users SET password_hash = %s WHERE iduser = %s"
            # Parameter
            values = [bytearray.fromhex(Password_hash), iduser]

            # SQL ausführen
            with connection.cursor() as cursor:
                cursor.execute(sql, values)
                
            Message = "Password changed succesfully"
            Status = 200
        except:
            Message = "Cant set password!"
            
        return Status, Message
    
class donationrecord(models.Model):
    donationrecid = models.IntegerField(primary_key=True, null=False)
    iduser = models.IntegerField(null=False)
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
    iscertreq = models.BooleanField(null=False)
    
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
                if row.verified == True:
                    #Calculate total Donations 
                    if (row.fixedamount == True):
                        # only add up the fixed dons if the user has atleast on km
                        if (kilometers > 0):
                            TotalDonations += row.donation
                    else:
                        TotalDonations += (row.donation * kilometers)
            
        except:
            print("Can't calculate without data")
        
        data = []
        #Safe evaluation
        data.append({
            "UserFirstname": UserFirstname,
            "UserLastname": UserLastname,
            "UserEmail": UserEmail,
            "TotalDonations": TotalDonations,
            "TotalKilometers": kilometers})
        
        #if (kilometers): 
            # Schleife durch die UserEntrys-Objekte
        for obj in UserEntrys:
                data.append({
                "donoid" : obj.donationrecid,
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
                "iscertreq": obj.iscertreq,
                })

        #return JSON 
        return data
    
    def GetAdminStats(Userid):
        #vars
        Message = "Permission denied"
        data = []
        #Get Userdata for welcome screen 
        UserName = Users.objects.raw("Select iduser, firstname, lastname, email From api_users Where iduser = %s", [Userid])
        
        Super_Data = donationrecord.objects.all()
        
        TDonoF = 0
        TDono = 0
        for Super_row in Super_Data:
            UserData = Users.objects.raw("Select iduser, kilometers From api_users Where iduser = %s",[Super_row.iduser])
            if (Super_row.fixedamount == True):
                # only add up the fixed dons if the user has atleast on km
                for user in UserData:
                    if user.kilometers > 0:
                        TDonoF += Super_row.donation
            else:
                for user in UserData:
                    TDono = TDono + (Super_row.donation * user.kilometers)
        
        for row in UserName:
            UserFirstname = row.firstname
            UserLastname = row.lastname
            UserEmail = row.email
            Roleid = row.roleid

        if (Roleid < 3):
            Message = "Permission granted"
        
        #Safe evaluation
        data.append({
            "DonoFix": TDonoF,
            "DonoTotal": TDono,
            "UserFirstname": UserFirstname,
            "UserLastname": UserLastname,
            "UserEmail": UserEmail,
            "Message": Message})


        if (Roleid == 1 or Roleid == 2):
            #Get Userdat 
            UserData = Users.objects.all().order_by('iduser')
            
            for row in UserData:
            
                data.append({"userid":row.iduser,
                            "firstname": row.firstname,
                            "lastname": row.lastname,
                            "email": row.email,
                            "createdat": row.createdat,
                            "verified": row.verified,
                            "kilometers": row.kilometers})
        
        return data
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

def convertSaltAndHash(salt, hash):
    return bytearray.fromhex(salt), bytearray.fromhex(hash) 

# Sets only the password not the salt
def PasswordSetJustPassword(password, salt):
    original_hex_string = salt.hex()
    Password_Hash = sha256((password + original_hex_string).encode('utf-8')).digest() 
    return Password_Hash.hex()          



def checkPwdConstraints(input_string):
    # 1 = valid, 0 = to short, -1 = missing later/digit/special char
    if len(input_string) < 8:
        return 0

    has_letter = any(char.isalpha() for char in input_string)
    has_digit = any(char.isdigit() for char in input_string)
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', input_string))

    if has_letter and has_digit and has_special:
        return 1
    else:
        return -1
    

def Generate_secure_password(length):
    if length < 8:
        raise ValueError("Passwortlänge sollte mindestens 8 Zeichen betragen.")
    
    allowed_special_chars = "!_-@%"  # Einschränkung auf 2 Sonderzeichen
    characters = string.ascii_letters + string.digits + allowed_special_chars
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

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