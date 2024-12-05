import smtplib
from django.shortcuts import get_object_or_404
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import pandas as pd
from . import views
from django.http import HttpResponse
from api.models import Users, donationrecord
from django.db.models import F, Sum, Case, When



###########Create Mail Interface############
# Create the file 'MailConfig.json' in this folder
# set the values sender_email and password. Like
# {
#     "sender_email":"test@test.de",
#     "password":"password123"
#     "smtp_server":"smtp.gmail.com",
#     "smtp_port":587
# }
# the smtp_port should be an integer
# the attributes behind _getData have to match the json!!!
###########################################


class getServerData:
    sender_email: str
    password: str
    smtp_server: str
    smtp_port: int
    def __init__(self):
        _getData = pd.read_json(f"{views.BASE_DIR}\Backend\CustomData\MailConfig.json", typ="series")
        print(_getData)
        # the attributes behind _getData have to match the json
        self.sender_email = _getData.sender_email
        self.password = _getData.password
        self.smtp_server = _getData.smtp_server
        self.smtp_port = _getData.smtp_port 
        print()
        print(self)
        print()
        print(self.sender_email)
        print("ServerData Load")

        
# translation_table = dict.fromkeys(map(ord, '"'), None) #Dont change



class MailSender():
    Server = None
    SD = None

    def __init__(self):
        self.SD = getServerData()
        print(self.SD)
        print(self.SD.sender_email)
        self.ConnectToServer()

    def ConnectToServer(self):
        print(self.SD.smtp_server)
        self.Server = smtplib.SMTP(host=self.SD.smtp_server, port=self.SD.smtp_port)
        self.Server.starttls()
        self.Server.login(user=self.SD.sender_email, password=self.SD.password)
        print("Connection to Mail-Server successfuly")

    def SendMail(self, pReceiver: str, pSubject: str, pIsAttachement: bool, pAttachement, pMailText: str):
        msg = MIMEMultipart()
        msg['Subject'] = pSubject
        msg['From'] = self.SD.sender_email
        msg['To'] = pReceiver

        #Get Messagebody
        # for i in MailTexts:
        #     MailTxt = str(GetText(i, Mailbody_File))
        #     Mailbody += MailTxt
        
        print(pMailText)
        msg.attach(MIMEText(pMailText, 'html', 'utf-8'))
        
        part = MIMEBase('application', "octet-stream")

        if pIsAttachement:
            part.set_payload(open(pAttachement, "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="Example_doc.pdf"')
            msg.attach(part)

        print(msg.as_string())
        Waiter = input("Waiting")
        



        try:
            self.Server.sendmail(self.SD.sender_email, pReceiver, msg.as_string())#"Subject: \n\n This is definitly not a Virus. Trust me bro: http://localhost:3000/register")
        except:
            print("Unexpected error ocurred while sending Mail!")
        
    # def generate

    def CloseConnection(self):
        self.Server.quit()
    




# decoded_html: str
# with urlopen(example_view()) as response:
#   html_response = response.read()
#   encoding = response.headers.get_content_charset('utf-8')
#   decoded_html = html_response.decode(encoding)
def sendUserVerifyMail(request, UserID):

    # print(views.BASE_DIR)
    # print(UserID)
    # _getData = pd.read_json(f"{views.BASE_DIR}\Backend\CustomData\MailConfig.json", typ="series")
    # print(_getData)

    # Fetch the user object from the database or raise a 404 error if not found
    user = get_object_or_404(Users, iduser=UserID)

    mail = MailSender()
    mail.SendMail(
        pReceiver=user.email, 
        pSubject="Anmeldung Spendenlauf", 
        pIsAttachement=False, 
        pMailText=views.UserAuth(request=request, UserID=UserID, user=user), 
        pAttachement="")
    
    mail.CloseConnection()

    return HttpResponse(f"Mail send to {user.lastname}, {user.firstname}")


def sendDonationVerifyMail(request, UserID, DonationId):

    # kann warscheinlich weg
    # print(views.BASE_DIR)
    # print(UserID)
    # _getData = pd.read_json(f"{views.BASE_DIR}\Backend\CustomData\MailConfig.json", typ="series")
    # print(_getData)

    # Fetch the user object from the database or raise a 404 error if not found
    user = get_object_or_404(Users, iduser=UserID)
    donRec = get_object_or_404(donationrecord, donationrecid=DonationId)

    mail = MailSender()
    mail.SendMail(
        pReceiver=donRec.email, 
        pSubject=f"Sponsoranmeldung für {user.lastname}, {user.firstname}", 
        pIsAttachement=False, 
        pMailText=views.DonRecAuth(request=request, UserID=UserID, user=user, DonRecID=DonationId,DonRec=donRec), 
        pAttachement="")
    
    mail.CloseConnection()

    return HttpResponse(f"Mail send to {user.lastname}, {user.firstname}")



class SponsData:
    firstname: str
    lastname: str
    kilometer: int
    FixedDonation: bool
    Donation: float
    DonationTotal: float
    def __init__(self, pFirstname, pLastname, pKm, pFixedDon, pDon):
        self.firstname = pFirstname
        self.lastname = pLastname
        self.kilometer = pKm
        self.FixedDonation = pFixedDon
        self.Donation = pDon
        if(pFixedDon):
            self.DonationTotal = pDon
        else:
            self.DonationTotal = pDon * pKm
        
def BinarySearchUsers(users, id):
    min = 0
    max = len(users)
    while min + 1 < max:
        index = min + (max - min) // 2
        val = users[index].iduser
        if(val == id):
            return index
        if(val < id):
            min = index
        else:
            max = index
    return -1;


# normal
def loadSponsorInfo(request, DonRecEmail, users):
    # user = get_object_or_404(Users, iduser=UserID)
    # donRec = get_object_or_404(donationrecord, email=DonRecEmail)
    donRec = donationrecord.objects.filter(email=DonRecEmail)

    print(donRec)
    mail = None
    TotalDonation: float
    TotalDonation = 0
    TotalKilometers = 0
    data = []
    for val in donRec:
        usersIndex = BinarySearchUsers(users, val.iduser)
        Kilometers = users[usersIndex].kilometers
        dataRec = SponsData(
            pFirstname=users[usersIndex].firstname, 
            pLastname=users[usersIndex].lastname, 
            pKm=Kilometers, 
            pFixedDon=val.fixedamount, 
            pDon=val.donation)
        
        TotalDonation += dataRec.DonationTotal
        TotalKilometers += Kilometers

        data.append(dataRec)

    context = {
            'name': f"{donRec[0].firstname} {donRec[0].lastname}",
            'Amount': len(donRec),
            'data': data,
            'Total': TotalDonation,
            'TotalKilometers': TotalKilometers,
        }

    print("test")
    print(context)
    print(donRec[0].firstname)


    tset = views.RenderMailText(context=context, request=request, template_name="SponsorInfo.html")
    print("tset")
    print(tset)
    return tset



# später die ganzen durch iterieren


def loadRunnerInfo(request, donRecs, user, RunnerAmount, EventKilometers, EventTotal):
    # user = get_object_or_404(Users, iduser=UserID)
    # donRec = get_object_or_404(donationrecord, email=DonRecEmail)

    mail = None
    Kilometers = user.kilometers
    SponsorAmount = 0
    data = []
    RunnerTotal: float
    RunnerTotal = 0

    for val in donRecs:
        # Check if the conatins the user
        if val.iduser != user.iduser:
            continue
        SponsorAmount += 1
        # usersIndex = BinarySearchUsers(users, val.iduser)
        dataRec = SponsData(
            pFirstname=val.firstname, 
            pLastname=val.lastname, 
            pKm=Kilometers, 
            pFixedDon=val.fixedamount, 
            pDon=val.donation)
        
        RunnerTotal += dataRec.DonationTotal

        data.append(dataRec)

    context = {
            'name': f"{user.firstname} {user.lastname}",
            'RunnerKilometers': Kilometers,
            'RunnerAmount': RunnerAmount,
            'SponsorAmount': SponsorAmount,
            'EventKilometers': EventKilometers,
            'EventTotal': EventTotal,
            'RunnerTotal': RunnerTotal,
            'data': data,
        }

    print("test")
    print(context)
    # print(donRec[0].firstname)


    tset = views.RenderMailText(context=context, request=request, template_name="RunnerInfo.html")
    print("tset")
    print(tset)
    return tset

def sendRunnerInfo(request):
    # Get only the runners (roleid == 3) which are verified
    users = Users.objects.filter(verified=True, roleid=3)
    donRecs = donationrecord.objects.all()
    #  get amount of runner

    
    RunnerAmount = users.count()    # Anzahl der Läufer
    # Kilometer aller Läufer
    EventKilometers = users.aggregate(total_km=Sum('kilometers'))['total_km'] or 0
    # Erlaufendes Geld aller Läufer
    EventTotal = 0
    print("test")
    # usersSortet = users.order_by("iduser")
    for donRec in donRecs.filter(verified=True):
        if donRec.fixedamount:
            EventTotal += donRec.donation
        else:
            print(donRec.iduser)
            km = 0
            try:
                # print("filter")
                # print(users.filter(iduser=donRec.iduser)[0].kilometers)
                km = users.get(iduser=donRec.iduser).kilometers
            except Exception as es:
                print("error ", es)

            EventTotal += donRec.donation * km

            

    print("test")
    print("RunnerAmount ", RunnerAmount)
    print("EventKilometers ", EventKilometers)
    print("EventTotal ", EventTotal)
    print("-----")
    mail = MailSender()
    for usr in users:
        mail.SendMail(
            pReceiver=usr.email, 
            pSubject="Spendenlauf Spenden Informationen", 
            pIsAttachement=False, 
            pMailText=loadRunnerInfo(request=request, 
                                     user=usr, donRecs=donRecs, 
                                     EventTotal=EventTotal, RunnerAmount=RunnerAmount, 
                                     EventKilometers=EventKilometers), 
            pAttachement="")

    mail.CloseConnection() 

    return HttpResponse("Mail send!")


# def sendSponsorInfo(request):
#     users = Users.objects.all()
#     donRecs = donationrecord.objects.all()
    
#     print(users)

#     mail = MailSender()

#     for usr in users:
#         mail.SendMail(
#             pReceiver=usr.email, 
#             pSubject="Spendenlauf Spenden Informationen", 
#             pIsAttachement=False, 
#             pMailText=loadSponsorInfo(request=request, donRecs=donRecs, user=usr), 
#             pAttachement="")

#     mail.CloseConnection() 

#     return HttpResponse("Mail send!")


def sendSponsorInfo(request):
    users = Users.objects.order_by("iduser")
    eMailArr = donationrecord.objects.values_list('email', flat=True).distinct()
    
    print(users)

    mail = MailSender()

    for eMail in eMailArr:
        mail.SendMail(
            pReceiver=eMail, 
            pSubject="Spendenlauf Spenden Informationen", 
            pIsAttachement=False, 
            pMailText=loadSponsorInfo(request=request, DonRecEmail=eMail, users=users), 
            pAttachement="")

    mail.CloseConnection() 

    return HttpResponse("Mail send!")


