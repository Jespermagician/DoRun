"""
Database models for the DoRun charity run application.

Defines the Users, donationrecord, and roles models along with
their business logic methods for registration, login, and statistics.
"""
from .password import pwd
from django.db import models
from datetime import date
from django.shortcuts import redirect
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import logout
from django.http import JsonResponse
import array
from django.db import connection


class Users(models.Model):
    """User model representing registered participants and admins.

    Stores user profile data, authentication credentials (hashed password + salt),
    role-based permissions, and activity tracking (kilometers, login attempts).

    Fields:
        iduser: Primary key, manually assigned integer ID
        firstname/lastname: User's name
        email: Unique email address
        password_hash: Binary hash of the salted password
        salt: Random binary salt for password hashing
        createdat: Auto-set on creation
        roleid: 1=admin, 2=moderator, 3=regular user
        kilometers: Total kilometers run by the user
        verified: Whether the user's email has been verified
        logintrys: Count of consecutive failed login attempts (locked at >5)
    """
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

    def RegisterUser(first_name, last_name, email, password):
        """
        Register a new user in the database.

        Validates password constraints, checks for duplicate emails,
        auto-assigns the next available user ID, hashes the password,
        and creates the database record.

        Args:
            first_name: User's first name
            last_name: User's last name
            email: User's email address (checked for uniqueness)
            password: Plaintext password to hash and store

        Returns:
            Users instance on success, None on validation failure or
            if required fields are missing.
        """
        # Validate password meets complexity requirements
        validation = pwd.checkPwdConstraints(password)
        if validation != 1:
            print("Password is not valid")
            return None

        # Step 1: Determine UserID — auto-increment from max existing ID
        email_exists = False
        UserID = None

        # Check if email already exists in the database
        try:
            duplicate_check = Users.objects.raw(
                "SELECT * FROM api_users WHERE email = " + "'" + email + "'"
            )
            for user_row in duplicate_check:
                email_exists = True
        except:
            email_exists = False

        print("duplicate email: " + str(email_exists))

        try:
            if email_exists == False:
                # Get current highest iduser to compute next ID
                query = "SELECT iduser FROM api_users WHERE iduser = (SELECT MAX(iduser) FROM api_users)"
                max_user_result = Users.objects.raw(query)

                # Check if there is at least one existing user
                has_existing_user = False
                for user_row in max_user_result:
                    has_existing_user = True
                    if user_row.iduser is not None:
                        UserID = user_row.iduser + 1
                    else:
                        UserID = 1

                print("has existing users: " + str(has_existing_user))

        except:
            print("Unexpected error occurred!")

        # Step 2: Hash the password with a random salt
        if password is not None:
            Password_hash, Salt = pwd.PasswordHashing(password)

        # Step 3: Set creation date to today
        CreatedAt = date.today()

        # Step 4: Default role is 3 (regular user)
        RoleID = 3

        # Step 5: Initialize defaults for new users
        Kilometers = 0
        VerifiedUser = False

        NewUser = None

        # Create new DB entry only if all required values are populated
        if (UserID is not None and first_name is not None and last_name is not None
                and email is not None and Password_hash is not None
                and Salt is not None and CreatedAt is not None and RoleID is not None):

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
                kilometers=Kilometers
            )
            return NewUser
        else:
            print("Not all requirements are fulfilled to create a user")

        # Registration denied — return None
        return None

    def LoginUser(email, password):
        """
        Authenticate a user by email and password.

        Looks up the user by email, compares the hashed password,
        tracks login attempts, and locks the account after 5 failures.

        Args:
            email: User's email address
            password: Plaintext password to verify

        Returns:
            Users instance on successful login.
            -101 if password is wrong or another error occurred.
            -100 if the account is locked (too many attempts).
        """
        # Using %s parameterized queries to prevent SQL injection
        try:
            # Fetch user data for the provided email
            matched_users = Users.objects.raw(
                "SELECT * FROM api_users WHERE email = %s", [email]
            )
            for user_row in matched_users:
                # Check for empty/initialized password
                empty_password = str(b'')

                # If stored password equals empty bytes, user has no password set
                if str(user_row.password_hash) == empty_password:
                    print(user_row.password_hash, empty_password)
                    print("No password set for user")
                    return -101

                # Hash the entered password with the stored salt and compare
                password_correct = pwd.CheckPassword(
                    password, user_row.password_hash, user_row.salt
                )

                login_attempts = user_row.logintrys

                if password_correct:
                    # Password matches — reset login attempts on success
                    if login_attempts <= 5:
                        login_attempts = 0

                        # Reset login counter in database via parameterized UPDATE
                        sql = "UPDATE api_users SET logintrys = %s WHERE email = %s"
                        values = [login_attempts, email]

                        try:
                            with connection.cursor() as cursor:
                                cursor.execute(sql, values)
                        except:
                            return -101

                        return user_row
                    else:
                        # Account is already locked
                        return -100
                else:
                    # Password incorrect — increment login attempts
                    login_attempts = login_attempts + 1

                    sql = "UPDATE api_users SET logintrys = %s WHERE email = %s"
                    values = [login_attempts, email]

                    try:
                        with connection.cursor() as cursor:
                            cursor.execute(sql, values)

                        if login_attempts > 5:
                            # Account locked after exceeding attempt limit
                            return -100
                        return -101
                    except:
                        return -101

        except:
            print("Error during login")


class donationrecord(models.Model):
    """Donation/sponsor record linking donors to runners.

    Tracks donation pledges: a sponsor (identified by name/email/address)
    pledges an amount per kilometer or a fixed amount for a specific runner.

    Fields:
        donationrecid: Primary key, manually assigned integer ID
        iduser: Foreign key reference to the sponsored runner
        firstname/lastname/email: Sponsor contact information
        street/housenr/postcode: Sponsor address
        donation: Pledged amount (per km if fixedamount=False, total if True)
        fixedamount: Whether the donation is a flat amount (True) or per-km (False)
        createdat: Auto-set on creation
        verified: Whether the donation has been verified
        iscertreq: Whether a donation certificate is requested
    """
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
        """
        Build dashboard data for a specific user.

        Retrieves the user's profile, all their donation records,
        and calculates total donations and total kilometers.

        For fixed-amount donations: only counted if the user has run at least 1 km.
        For per-km donations: donation amount multiplied by user's kilometers.

        Args:
            Userid: The user's ID

        Returns:
            List of dicts with user info, totals, and donation entry details.
            Returns False if data cannot be computed.
        """
        # Fetch user profile data
        UserName = Users.objects.raw(
            "SELECT iduser, firstname, lastname, email FROM api_users WHERE iduser = %s",
            [Userid]
        )

        for row in UserName:
            UserFirstname = row.firstname
            UserLastname = row.lastname
            UserEmail = row.email

        # Fetch all donation records for this user
        UserDonations = donationrecord.objects.raw(
            "SELECT * FROM api_donationrecord WHERE iduser = %s", [Userid]
        )

        # Fetch complete user data (needed for kilometers)
        UserData = Users.objects.raw(
            "SELECT * FROM api_users WHERE iduser = %s", [Userid]
        )

        TotalDonations = 0
        TotalKilometers = 0

        # Get total kilometers for the user
        for row in UserData:
            kilometers = row.kilometers

        try:
            for row in UserDonations:
                if row.verified == True:
                    if row.fixedamount == True:
                        # Fixed donations only count if the user has at least 1 km
                        if kilometers > 0:
                            TotalDonations += row.donation
                    else:
                        # Per-km donations: amount * kilometers run
                        TotalDonations += (row.donation * kilometers)
        except:
            print("Can't calculate without data")

        data = []

        # Add summary row with totals
        data.append({
            "UserFirstname": UserFirstname,
            "UserLastname": UserLastname,
            "UserEmail": UserEmail,
            "TotalDonations": TotalDonations,
            "TotalKilometers": kilometers
        })

        # Add individual donation record details
        for donation_entry in UserDonations:
            data.append({
                "donoid": donation_entry.donationrecid,
                "firstname": donation_entry.firstname,
                "lastname": donation_entry.lastname,
                "email": donation_entry.email,
                "street": donation_entry.street,
                "housenr": donation_entry.housenr,
                "postcode": donation_entry.postcode,
                "donation": donation_entry.donation,
                "fixedamount": donation_entry.fixedamount,
                "createdat": date.today(),
                "verified": donation_entry.verified,
                "Kilometer": kilometers,
                "iscertreq": donation_entry.iscertreq,
            })

        return data

    def GetAdminStats(Userid):
        """
        Build admin dashboard data.

        Retrieves aggregate donation statistics across all records,
        plus the admin's own profile info. For admin users (roleid < 3),
        also returns the full user list.

        Fixed donations are only counted for runners with at least 1 km.

        Args:
            Userid: The admin's user ID

        Returns:
            List of dicts with donation totals, admin info, and
            (for admins) full user list.
        """
        data = []

        # Fetch admin user profile
        UserName = Users.objects.raw(
            "SELECT iduser, firstname, lastname, email FROM api_users WHERE iduser = %s",
            [Userid]
        )

        # Get all donation records for aggregate calculations
        AllDonations = donationrecord.objects.all()

        TDonoF = 0   # Total of fixed donations
        TDono = 0    # Total of per-km donations

        for donation_row in AllDonations:
            # Fetch the runner's kilometers for this donation
            UserData = Users.objects.raw(
                "SELECT iduser, kilometers FROM api_users WHERE iduser = %s",
                [donation_row.iduser]
            )

            if donation_row.fixedamount == True:
                # Fixed donations only count if runner has at least 1 km
                for user in UserData:
                    if user.kilometers > 0:
                        TDonoF += donation_row.donation
            else:
                # Per-km donations: amount * runner's kilometers
                for user in UserData:
                    TDono = TDono + (donation_row.donation * user.kilometers)

        # Extract admin profile fields
        for row in UserName:
            UserFirstname = row.firstname
            UserLastname = row.lastname
            UserEmail = row.email
            Roleid = row.roleid

        message = "Permission denied"
        if Roleid < 3:
            message = "Permission granted"

        # Add summary row
        data.append({
            "DonoFix": TDonoF,
            "DonoTotal": TDono,
            "UserFirstname": UserFirstname,
            "UserLastname": UserLastname,
            "UserEmail": UserEmail,
            "Message": message
        })

        # Admins (roleid 1 or 2) also receive the full user list
        if Roleid == 1 or Roleid == 2:
            # Fetch all users ordered by ID
            AllUsers = Users.objects.all().order_by('iduser')

            for row in AllUsers:
                data.append({
                    "userid": row.iduser,
                    "firstname": row.firstname,
                    "lastname": row.lastname,
                    "email": row.email,
                    "createdat": row.createdat,
                    "verified": row.verified,
                    "kilometers": row.kilometers
                })

        return data


def roles():
    """Role model definition (placeholder — not yet implemented as a DB table)."""
    roleid = models.IntegerField(primary_key=True, null=False)
    rolename = models.TextField(null=False)


class CustomBackend(BaseBackend):
    """Custom authentication backend stub for Django auth integration."""
    def get_user(self, user_id):
        return Users(id=user_id, username='benutzername')
