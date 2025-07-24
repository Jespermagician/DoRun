from hashlib import sha256
from multiprocessing import connection
import random
import string
import re
from . import models



class pwd():
    def SetPassword(email,Password):
        Message = ""
        Status = 401
        try:
            Password_hash, Salt = pwd.PasswordHashing(Password)
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
    
        match pwd.checkPwdConstraints(Password):
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
            salt = models.Users.objects.get(iduser=iduser).salt
            print("salt: ", salt)
            Password_hash = pwd.PasswordSetJustPassword(password=Password, salt=salt)

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
    

    # Method to create string of random chars
    def RandChars(size=30, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def PasswordHashing(password):
        SaltText = pwd.RandChars()                                              # Generiert zufällige Zeichenabfolge   
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
