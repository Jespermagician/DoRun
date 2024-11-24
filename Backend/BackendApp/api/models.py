from django.db import models
from datetime import date
from django.shortcuts import redirect
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import logout, authenticate, login

# Create your models here.
class Users(models.Model):
    iduser = models.IntegerField(primary_key=True, null=False)
    firstname = models.TextField(null=False)
    lastname = models.TextField(null=False)
    email = models.EmailField(unique=False, null=False)
    password_hash = models.BinaryField(null=False)  # Manuelles Hashing erforderlich
    salt = models.BinaryField(null=False)
    createdat = models.DateTimeField(auto_now_add=True, null=False)
    roleid = models.IntegerField(null=False)
    verifieduser = models.BooleanField()
 
    def RegisterUser(first_name,last_name,email,password):
        #Set UserID
        try:
            query = "Select iduser From api_users Where iduser = (Select Max(iduser) From api_users)"
            user = Users.objects.raw(query)

            for p in user:
                if (p.iduser != None):
                    UserID = p.iduser
                    UserID = UserID + 1
                elif (p.iduser == None):
                    UserID = 1
                    
        except:
            print("Unexpected error ocurred!")
        
        #Password hashing
        if (password != None):
            Password_hash, Salt = PasswordHashing(password)
            
        #Set current date 
        CreatedAt = date.today()
        
        #Set RoleID = 3 aka User
        RoleID = 3 
        
        #Set user-validation validation set by Link to true
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
            LoginUser = Users.objects.raw("Select * From api_users Where email = %s", [email])
            
            for p in LoginUser:
                check_password = DecryptPassword(password,p.salt)
                
                if (check_password == password):
                    return redirect('home')
        
        except:
            print("Error")
            
                    
        

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
    logout(request)
    return redirect('login')
