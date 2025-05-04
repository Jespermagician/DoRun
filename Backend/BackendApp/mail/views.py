from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from pathlib import Path
from hashlib import sha256
from django.shortcuts import get_object_or_404
from api.models import Users, donationrecord
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from . import mail_handle
from datetime import datetime
import json

# The base directory for the "DoRun" project
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

@csrf_protect
def SendInfoMailsSponsors(request):
    if request.method == 'POST':

        mail_handle.sendSponsorInfo(request=request)
        try:
            print("tsd")
        except: 
            return HttpResponse("Mails Couldn't be send to the Sponsors", status=401)
        
    
        return HttpResponse("Mails Send to Sponsors", status=200)
    
@csrf_protect
def SendInfoMailsRunners(request):
    if request.method == 'POST':

        try:
            mail_handle.sendRunnerInfo(request=request)
        except: 
            return HttpResponse("Mails could not be send to the Runner", status=401)
        
    
        return HttpResponse("Mails Send to Verified Runners", status=200)


# A simple index view that returns a plain text response
@csrf_protect
def indexMail(request):
    return HttpResponse("Hello... ")

# Function to generate a secure token using SHA-256
def generateToken(pSalt, pEMail):
    token = sha256(str(str(pEMail) + str(pSalt)).encode('utf-8')).hexdigest()
    # print("token: ", token)  # Debug: print the generated token
    return token

def RenderMailText(context, template_name, request):
    try:
        # Render the HTML content using the specified template and context
        rendered_html = render_to_string(template_name=template_name, context=context, request=request)

        # Return the rendered HTML content
        print("rendered_html")
        print(rendered_html)
        return rendered_html

    except FileNotFoundError:
        # Handle the case where the template file is not found
        print(f"The file '{template_name}' was not found.")
    except Exception as e:
        # Catch and print any other errors
        print(f"An error occurred: {e}")
        return None


# Function for user authentication email generation
def UserAuth(request, UserID: int, user, frontendDomain: str):
    
    # Path to the template file
    template_name_html = "UserAuth.html"
    template_name_plain = "UserAuth-plain.txt"

    # generate Timstamp, so the token has a ttl later
    dt_timestamp = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
    epoch_time = int(dt_timestamp.timestamp() * 1000)  # Millisekunden-Genauigkei

    # Base-16 umwandeln (Hexadezimal)
    compressed = format(epoch_time, 'x')  # Beispiel: "1944bc7a51"
    print("Compressed String:", compressed)

    # Generate a token for the user
    token = generateToken(user.salt, user.email)
    # compressed_token = format(int(token, 16), 'x')  # Hexadezimal umwandeln
    # print("Compressed Token:", compressed_token)

    # Construct the full URL for the authentication link
    target_link = f"https://{frontendDomain}/auth/user/{UserID}/{token}/{compressed}"  # Append the path with UserID and token

    # old target link (obsolet)
    # domain = request.build_absolute_uri('/')[:-1]  # Get the domain without trailing slash
    # target_link = f"{domain}/mail/auth/{UserID}/{token}"  # Append the path with UserID and token


    print("target_link: ", target_link)  # Debug: print the generated link

    # Context for rendering the email template
    context = {
        'name': f"{user.firstname} {user.lastname}",  # User's full name
        'link_url': target_link  # Authentication link
    }
    return RenderMailText(context, template_name_html, request), RenderMailText(context, template_name_plain, request);


def DonRecAuth(request, UserID: int, user, DonRecID: int, DonRec, frontendDomain: str):
    
    # Path to the template file
    template_name_html = "DonRecAuth.html"
    template_name_plain = "DonRec-plain.txt"
    

    # Generate a token for the user. conacte both mails (otherwise the token isn`t unique)
    token = generateToken(user.salt, '-'.join(user.email + DonRec.email))

    target_link = f"https://{frontendDomain}/auth/don/{UserID}/{DonRecID}/{token}"  # Append the path with UserID and token

    # old way to get the domain
    # domain = request.build_absolute_uri('/')[:-1]  # Get the domain without trailing slash
    # target_link = f"{domain}/mail/auth/don/{UserID}/{DonRecID}/{token}"  # Append the path with UserID and token

    print("target_link: ", target_link)  # Debug: print the generated link

    # Context for rendering the email template
    context = {
        'RunnerName': f"{user.firstname} {user.lastname}",  # Runners's full name
        'name': f"{DonRec.firstname} {DonRec.lastname}",  # Sponsors's full name
        'Donation': DonRec.donation,  # Authentication link
        'FixesDonation': DonRec.fixedamount,  # Authentication link
        'link_url': target_link  # Authentication link
    }
    return RenderMailText(context, template_name_html, request), RenderMailText(context, template_name_plain, request);


def ForgotPwd_MailBody(request, email, frontendDomain: str, user):
   # Path to the template file
    template_name = "ForgotPwdMail.html"

    # Generate a token for the user. conacte both mails (otherwise the token isn`t unique)
    token = generateToken(user.salt, '-'.join(email))

    # generate Timstamp, so the token has a ttl later
    dt_timestamp = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
    epoch_time = int(dt_timestamp.timestamp() * 1000)  # Millisekunden-Genauigkei
    
    # Convert to Base-16 (Hexadecimal)
    compressed = format(epoch_time, 'x')  # Beispiel: "1944bc7a51"

    target_link = f"https://{frontendDomain}/auth/pwd/{user.iduser}/{token}/{compressed}"  # Append the path with UserID and token

    # old way to get the domain
    # domain = request.build_absolute_uri('/')[:-1]  # Get the domain without trailing slash
    # target_link = f"{domain}/mail/auth/don/{UserID}/{DonRecID}/{token}"  # Append the path with UserID and token

    print("target_link: ", target_link)  # Debug: print the generated link

    # Context for rendering the email template
    context = {
        'link_url': target_link  # Authentication link
    }
    return RenderMailText(context, template_name, request);


@csrf_protect
def verify_user(request, UserID, token, TimeStamp):
    # Suche nach dem Benutzer mit der ID
    user = get_object_or_404(Users, iduser=UserID)

    # get TimeStamp and use it later for ttl
    epoch_time_back = int(TimeStamp, 16)
    TimeStampVerification = datetime.fromtimestamp(epoch_time_back / 1000)
    print("TimeStampVerification: ", TimeStampVerification)
    # return JsonResponse({"message": "EXPIRED"}, status=400)
     
    # Token neu generieren
    compared_token = generateToken(user.salt, pEMail=user.email)
    # Token vergleichen
    if compared_token == token:
        if user.verified:
            print("Nutzer bereits verifiziert!")
            return JsonResponse({"message": "VERIFIED"}, status=200)

        # Verifizieren und speichern
        user.verified = True
        user.save()
        print("User is verified!")
        return JsonResponse({"message": "VERIFIED"}, status=200)
    else:
        return JsonResponse({"message": "INVALID"}, status=400)
        # return HttpResponse("Ungültiger Token oder Benutzer nicht gefunden.", status=400)
    


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
            return JsonResponse({"message": "VERIFIED"}, status=200)

        # Verifizieren und speichern
        donRec.verified = True
        donRec.save()
        print("Spendenbereitschaft erfolgreich verifiziert!")
        return JsonResponse({"message": "VERIFIED"}, status=200)
    else:
        return JsonResponse({"message": "INVALID"}, status=400)
    

    
@csrf_protect
def send_new_pwd(request):
    json_data = json.loads(request.body)
    email = json_data["email"]
    frontendDomain = json_data["frontendDomain"]
    if request.method == 'POST':
        try:
            mail_handle.sendForgotPwd(request=request, email=email, frontendDomain=frontendDomain)
        except: 
            return HttpResponse("Mail could not be send to the User", status=401)

    return HttpResponse("Mail Send to Change Pwd", status=200)
