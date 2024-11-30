import string
import random
from django.template.loader import render_to_string
from django.http import HttpResponse
from pathlib import Path
from hashlib import sha256
from django.shortcuts import get_object_or_404
from api.models import Users, donationrecord

# The base directory for the "DoRun" project
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# A simple index view that returns a plain text response
def indexMail(request):
    return HttpResponse("Hello... ")

# Function to generate a secure token using SHA-256
def generateToken(pSalt, pEMail):
    token = sha256(str(str(pEMail) + str(pSalt)).encode('utf-8')).hexdigest()
    print("token: ", token)  # Debug: print the generated token
    return token

def RenderMailText(context, template_name, request):
    try:
        # Render the HTML content using the specified template and context
        rendered_html = render_to_string(template_name=template_name, context=context, request=request)

        # Return the rendered HTML content
        return rendered_html

    except FileNotFoundError:
        # Handle the case where the template file is not found
        print(f"The file '{template_name}' was not found.")
    except Exception as e:
        # Catch and print any other errors
        print(f"An error occurred: {e}")
        return None


# Function for user authentication email generation
def UserAuth(request, UserID: int, user):
    
    # Path to the template file
    template_name = "UserAuth.html"

    # Generate a token for the user
    token = generateToken(user.salt, user.email)

    # Construct the full URL for the authentication link
    domain = request.build_absolute_uri('/')[:-1]  # Get the domain without trailing slash
    target_link = f"{domain}/mail/auth/{UserID}/{token}"  # Append the path with UserID and token

    print("target_link: ", target_link)  # Debug: print the generated link

    # Context for rendering the email template
    context = {
        'name': f"{user.firstname} {user.lastname}",  # User's full name
        'link_url': target_link  # Authentication link
    }
    return RenderMailText(context, template_name, request);


def DonRecAuth(request, UserID: int, user, DonRecID: int, DonRec):
    
    # Path to the template file
    template_name = "DonRecAuth.html"

    # Generate a token for the user. conacte both mails (otherwise the token isn`t unique)
    token = generateToken(user.salt, '-'.join(user.email + DonRec.email))

    # Construct the full URL for the authentication link
    domain = request.build_absolute_uri('/')[:-1]  # Get the domain without trailing slash
    target_link = f"{domain}/mail/auth/don/{UserID}/{DonRecID}/{token}"  # Append the path with UserID and token

    print("target_link: ", target_link)  # Debug: print the generated link

    # Context for rendering the email template
    context = {
        'RunnerName': f"{user.firstname} {user.lastname}",  # Runners's full name
        'name': f"{DonRec.firstname} {DonRec.lastname}",  # Sponsors's full name
        'Donation': DonRec.donation,  # Authentication link
        'FixesDonation': DonRec.fixedamount,  # Authentication link
        'link_url': target_link  # Authentication link
    }
    return RenderMailText(context, template_name, request);


def verify_user(request, UserID, token):
    # Suche nach dem Benutzer mit der ID
    user = get_object_or_404(Users, iduser=UserID)

    # Token neu generieren
    compared_token = generateToken(user.salt, pEMail=user.email)
    # Token vergleichen
    if compared_token == token:
        if user.verified:
            print("Nutzer bereits verifiziert!")
            return HttpResponse("Nutzer bereits verifiziert!")

        # Verifizieren und speichern
        user.verified = True
        user.save()
        print("Benutzer erfolgreich verifiziert!")
        return HttpResponse("Benutzer erfolgreich verifiziert!")
    else:
        return HttpResponse("Ungültiger Token oder Benutzer nicht gefunden.", status=400)
    


def verify_donRec(requst, UserID, DonRecID, token):
        # Suche nach dem Benutzer mit der ID
    user = get_object_or_404(Users, iduser=UserID)
    donRec = get_object_or_404(donationrecord, donationrecid=DonRecID)

    # Token neu generieren
    compared_token = generateToken(user.salt, '-'.join(user.email + donRec.email))

    # Token vergleichen
    if compared_token == token:
        if donRec.verified:
            print("Spendenbereitschaft bereits verifiziert!")
            return HttpResponse("Spendenbereitschaft bereits verifiziert!")

        # Verifizieren und speichern
        donRec.verified = True
        donRec.save()
        print("Spendenbereitschaft erfolgreich verifiziert!")
        return HttpResponse("Spendenbereitschaft erfolgreich verifiziert!")
    else:
        return HttpResponse("Ungültiger Token oder Benutzer oder Spendeneintrag nicht gefunden.", status=400)