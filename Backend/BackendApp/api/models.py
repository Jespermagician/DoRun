from django.db import models
from datetime import date
from django.shortcuts import redirect
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import logout
from django.http import JsonResponse
import json

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
    verifieduser = models.BooleanField()
    
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
        VerifiedUser = False
        
        #Creat new DB entry if values are filled    
        if (UserID != None and first_name != None and last_name != None and email != None and Password_hash != None and Salt != None and CreatedAt != None and RoleID != None):
            try:
                print("Creating new User with ID: " + str(UserID))
                NewUser = Users.objects.create(iduser=UserID, firstname=first_name,lastname=last_name,email=email,password_hash=Password_hash,salt=Salt,createdat=CreatedAt,roleid=RoleID,verifieduser=VerifiedUser)
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
                check_password = DecryptPassword(password,p.salt)
                
                #Check if given password = password from DB 
                if (check_password == password):
                    #Return LoginUser
                    return p
        
        except:
            print("Error")
            
class donationrecords():
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
        
        #Get donationrecords for the loggedin user
        UserEntrys = donationrecords.objects.raw("Select * From api_donationrecords Where iduser = %s", [Userid])
        
        TotalDonations = 0
        TotalKilometers = 0
        #Get Total amount for Donations and Total Kilometers 
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

def PasswordHashing(password):
    Password_Hash = bytes(1)
    Salt = bytes(2)

    return Password_Hash, Salt

# end def

def DecryptPassword(password,salt):
    decryptedPassword = str(1)
    
    return decryptedPassword

class CustomBackend(BaseBackend):
    def get_user(self, user_id):
        # Optional: Benutzer anhand der ID aus deiner Datenbank holen
        return Users(id=user_id, username='benutzername')

def user_logout(request):
    #Reset acces 
    request.session["iduser"] = 0
    request.session["UserIsAuth"] = False
    return redirect('login')