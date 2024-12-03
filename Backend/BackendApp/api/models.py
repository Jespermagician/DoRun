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
        
        #
        #5. Set user-validation validation set by Link to true
        Kilometers = 0
        VerifiedUser = False
        
        #Creat new DB entry if values are filled    
        if (UserID != None and first_name != None and last_name != None and email != None and Password_hash != None and Salt != None and CreatedAt != None and RoleID != None):
            try:
                print("Creating new User with ID: " + str(UserID))
                NewUser = Users.objects.create(iduser=UserID, firstname=first_name,lastname=last_name,email=email,password_hash=Password_hash,salt=Salt,createdat=CreatedAt,roleid=RoleID,verified=VerifiedUser, kilometers=Kilometers)
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
                # Enter the entered password encrypt it with the salt and compare it with the pwhash from the db
                if (CheckPassword(password, p.password_hash, p.salt) ):
                    #Return LoginUser
                    return p
        
        except:
            print("Error")
            
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
        UserName = Users.objects.raw("Select firstname, lastname, email From api_users Where iduser = %s", [Userid])
        
        for row in UserName:
            UserFirstname = row.firstname
            UserLastname = row.lastname
            UserEmail = row.email
        
        #Get donationrecord for the loggedin user
        UserEntrys = donationrecord.objects.raw("Select * From api_donationrecord Where iduser = %s", [Userid])
        
        TotalDonations = 0
        TotalKilometers = 0
        #Get Total amount for Donations and Total Kilomers 
        for row in UserEntrys:
            #Calculate total Donations 
            if (row.fixedamount == True):
                TotalDonations += row.donation
            else:
                TotalDonations = TotalDonations + (row.donation * row.kilometers)
            
            TotalKilometers += row.kilometers
        
        data = [
            {
             "UserFirstname": UserFirstname,
             "UserLastname": UserLastname,
             "UserEmail": UserEmail,
             "firstname": obj.firstname, "lastname": obj.lastname, 
             "email": obj.email, "street": obj.street, 
             "housenr": obj.housenr,"postcode": obj.postcode, 
             "donation": obj.donation, "fixedamount": obj.fixedamount, 
             "createdat": obj.createdat, "verified": obj.verified, 
             "Kilometers": obj.kilometers,  
             "TotalDonations": TotalDonations,"TotalKilometers": TotalKilometers}  # Felder anpassen
            for obj in UserEntrys
        ]

        return JsonResponse(status=200, data={data})
            
def roles():
    roleid = models.IntegerField(primary_key=True,null=False)
    rolename = models.TextField(null=False)

# Method to create string of random chars
def RandChars(size=30, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def PasswordHashing(password):
    SaltText = RandChars()  # Generate string as salt
    Salt = sha256(SaltText.encode('utf-8')).digest()  # Generate binary salt
    Password_Hash = sha256((password + Salt.hex()).encode('utf-8')).digest()  # Hash password + salt
    return Password_Hash, Salt

def CheckPassword(EnteredPwd, password, salt):
    # Recalculate hash for the entered password
    EnteredPwdHash = sha256((EnteredPwd + salt.hex()).encode('utf-8')).digest()
    print("Calculated Hash:", EnteredPwdHash)

    # Compare hashes
    is_valid = EnteredPwdHash == password
    print("Password Match:", is_valid)
    return is_valid



# e
# def CheckPassword(EnteredPwd, password,salt):
#     print("--------------------")
#     print("--------------------")
#     print("--------------------")
#     print("--------------------")
#     print(salt)
#     print(str(salt))
#     print("--------------------")


#     print("EnteredPwd ", EnteredPwd)
#     print("pass ", password)
#     EnteredPwdHashes = sha256(''.join(EnteredPwd + str(salt)).encode('utf-8')).hexdigest()
#     print("EnteredPwdHashes ", EnteredPwdHashes)
#     test = sha256(''.join(EnteredPwd + str(salt)).encode('utf-8')).hexdigest()
#     print("hashTest ", test)
#     print("comp ", EnteredPwdHashes == password)

#     return EnteredPwdHashes == password

class CustomBackend(BaseBackend):
    def get_user(self, user_id):
        # Optional: Benutzer anhand der ID aus deiner Datenbank holen
        return Users(id=user_id, username='benutzername')

def user_logout(request):
    #Reset acces 
    request.session["iduser"] = 0
    request.session["UserIsAuth"] = False
    return redirect('login')