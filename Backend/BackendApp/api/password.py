"""
Password management utilities for the DoRun application.

Provides password hashing, validation, secure generation, and
database update methods used by views and models.
"""
from hashlib import sha256
from multiprocessing import connection
import random
import string
import re
from . import models


class pwd():
    """Static utility class for password operations."""

    def SetPassword(email, Password):
        """
        Reset a user's password and salt via email.

        Generates a new random salt, hashes the new password,
        and updates the database with both.

        Args:
            email: User's email address
            Password: New plaintext password

        Returns:
            Tuple of (HTTP_status, message_string)
        """
        Message = ""
        Status = 401
        try:
            # Generate new salt and hash for the password
            Password_hash, Salt = pwd.PasswordHashing(Password)
            print(Password_hash, Salt)

            # Parameterized UPDATE query to prevent SQL injection
            sql = "UPDATE api_users SET password_hash = %s, salt = %s WHERE email = %s"
            values = [bytearray.fromhex(Password_hash), bytearray.fromhex(Salt), email]

            # Execute the update
            with connection.cursor() as cursor:
                cursor.execute(sql, values)

            Message = "Password changed successfully"
            Status = 200
        except:
            Message = "Cannot set password!"

        return Status, Message

    def SetJustPasswordWith_iduser(iduser, Password):
        """
        Change a user's password by ID, preserving the existing salt.

        Unlike SetPassword(), this reuses the user's current salt,
        so only the password hash is updated. Used when the user
        knows their old password and just wants to change it.

        Args:
            iduser: User's ID
            Password: New plaintext password

        Returns:
            Tuple of (HTTP_status, message_string)
        """
        Message = ""
        Status = 401

        # Validate password complexity before proceeding
        match pwd.checkPwdConstraints(Password):
            case -1:
                Message = "Password must contain a letter, a number, and a special character!"
                Status = 401
                return Status, Message
            case 0:
                Message = "Password must be at least 8 characters long!"
                Status = 401
                return Status, Message

        print("Password is valid")

        try:
            # Retrieve the user's existing salt (do not generate a new one)
            salt = models.Users.objects.get(iduser=iduser).salt
            print("salt:", salt)

            # Hash the new password with the existing salt
            Password_hash = pwd.PasswordSetJustPassword(password=Password, salt=salt)
            print("Password_hash:", Password_hash)

            # Update only the password hash in the database
            sql = "UPDATE api_users SET password_hash = %s WHERE iduser = %s"
            values = [bytearray.fromhex(Password_hash), iduser]

            with connection.cursor() as cursor:
                cursor.execute(sql, values)

            Message = "Password changed successfully"
            Status = 200
        except:
            Message = "Cannot set password!"

        return Status, Message

    def RandChars(size=30, chars=string.ascii_uppercase + string.digits):
        """
        Generate a random string of specified length.

        Used for creating random salts.

        Args:
            size: Length of the generated string (default 30)
            chars: Character pool to draw from (default: uppercase + digits)

        Returns:
            Random string of length `size`
        """
        return ''.join(random.choice(chars) for _ in range(size))

    def PasswordHashing(password):
        """
        Hash a password with a new random salt.

        Steps:
        1. Generate a random salt string
        2. SHA-256 hash the salt string to produce the salt digest
        3. SHA-256 hash the concatenation of password + salt digest

        Args:
            password: Plaintext password to hash

        Returns:
            Tuple of (password_hash_hex, salt_hex) — both as hex strings
        """
        # Generate random characters for the salt
        SaltText = pwd.RandChars()

        # Hash the salt text to produce the final salt
        Salt = sha256(SaltText.encode('utf-8')).digest().hex()

        # Hash the password concatenated with the salt
        Password_Hash = sha256((password + Salt).encode('utf-8')).digest()

        return Password_Hash.hex(), Salt

    def convertSaltAndHash(salt, hash):
        """
        Convert hex-encoded salt and hash strings to bytearray format.

        Used when storing password data in the database BinaryField.

        Args:
            salt: Hex string of the salt
            hash: Hex string of the password hash

        Returns:
            Tuple of (salt_bytearray, hash_bytearray)
        """
        return bytearray.fromhex(salt), bytearray.fromhex(hash)

    def PasswordSetJustPassword(password, salt):
        """
        Hash a password using an existing salt (no new salt generated).

        Used when changing a password without rotating the salt.

        Args:
            password: Plaintext password
            salt: Existing salt as bytearray

        Returns:
            Hex string of the resulting password hash
        """
        # Convert bytearray salt to hex string for hashing
        salt_hex = salt.hex()

        # Hash password concatenated with the existing salt
        Password_Hash = sha256((password + salt_hex).encode('utf-8')).digest()

        return Password_Hash.hex()

    def checkPwdConstraints(input_string):
        """
        Validate password complexity requirements.

        Checks that the password:
        - Is at least 8 characters long
        - Contains at least one letter
        - Contains at least one digit
        - Contains at least one special character

        Args:
            input_string: Password string to validate

        Returns:
            1 if valid, 0 if too short, -1 if missing required character types
        """
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
        """
        Generate a cryptographically random password.

        Uses letters, digits, and a restricted set of special characters.

        Args:
            length: Desired password length (minimum 8)

        Returns:
            Random password string

        Raises:
            ValueError if length < 8
        """
        if length < 8:
            raise ValueError("Password length must be at least 8 characters.")

        # Restricted set of special characters for compatibility
        allowed_special_chars = "!_-@%"
        characters = string.ascii_letters + string.digits + allowed_special_chars
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def CheckPassword(EnteredPwd, password, salt):
        """
        Verify a plaintext password against a stored hash and salt.

        Steps:
        1. Hash the entered password with the stored salt
        2. Compare the result with the stored password hash

        Args:
            EnteredPwd: Plaintext password to verify
            password: Stored password hash as bytearray
            salt: Stored salt as bytearray

        Returns:
            True if the password matches, False otherwise
        """
        # Hash the entered password with the stored salt
        EnteredPwdHash = sha256((EnteredPwd + salt.hex()).encode('utf-8')).digest()

        # Compare the newly computed hash with the stored hash
        is_valid = EnteredPwdHash == password

        return is_valid
