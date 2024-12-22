import smtplib
from django.shortcuts import get_object_or_404
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
from . import views
from BackendApp import settings as set
from django.http import HttpResponse
from api.models import Users, donationrecord
from django.db.models import Sum



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
        set.logger.print(_getData)
        # the attributes behind _getData have to match the json
        self.sender_email = _getData.sender_email
        self.password = _getData.password
        self.smtp_server = _getData.smtp_server
        self.smtp_port = _getData.smtp_port 
        


class MailSender():
    Server = None  # SMTP-Verbindung zum Mail-Server
    SD = None      # Objekt, das Serverdaten wie Host, Port und Login-Daten enthält

    def __init__(self): 
        self.SD = getServerData()       # Funktion, die Serverdaten zurückgibt (nicht definiert im Code)
        self.ConnectToServer()
        set.logger.print("Server Started")

    def ConnectToServer(self):          # Stellt eine Verbindung zum SMTP-Server her
        self.Server = smtplib.SMTP(host=self.SD.smtp_server, port=self.SD.smtp_port)
        self.Server.starttls()                                                          # Aktiviert den TLS-Schlüssel
        self.Server.login(user=self.SD.sender_email, password=self.SD.password)         # Authentifizierung

    def SendMail(self, pReceiver: str, pSubject: str, pMailText: str):
        msg = MIMEMultipart()                               # Erstellt eine  Nachricht 
        msg['Subject'] = pSubject                           # Betreff
        msg['From'] = self.SD.sender_email                  # Absenderadresse
        msg['To'] = pReceiver                               # Empfängeradresse
        msg.attach(MIMEText(pMailText, 'html', 'utf-8'))    # Fügt den Nachrichtentext hinzu (HTML-formatiert)
        
        # Sende die vorbereitete Nachricht
        try:
            self.Server.sendmail(self.SD.sender_email, pReceiver, msg.as_string())  # Sendet die E-Mail
            set.logger.print("Mail sent")  # Rückgabe bei Erfolg
        except:
            set.logger.print("Unexpected error occurred while sending Mail!")  # Fehlerbehandlung 

    # Beendet die Verbindung zum Mail-Server
    def CloseConnection(self):
        self.Server.quit()
        set.logger.print("Disconnected from Mail Server")

    

def sendUserVerifyMail(request, UserID):
    user = get_object_or_404(Users, iduser=UserID)      # Bekomme einzelnen User anhand der ID

    
    mail = MailSender()     # Verbindung zum Mail Server erstellen

    # Absendung der Mail initiieren
    mail.SendMail(
        pReceiver=user.email, 
        pSubject="Anmeldung Spendenlauf", 
        pIsAttachement=False, 
        pMailText=views.UserAuth(request=request, UserID=UserID, user=user), 
        pAttachement="")
    
    mail.CloseConnection()      # Verbindung zum Server abbrechen

    return HttpResponse(f"Mail send to {user.lastname}, {user.firstname}")          # Http-Anwtort senden


def sendDonationVerifyMail(request, UserID, DonationId):
    user = get_object_or_404(Users, iduser=UserID)      # Bekomme einzelnen User anhand der ID
    donRec = get_object_or_404(donationrecord, donationrecid=DonationId)        # Bekomme einzelnen Spendeneintrag anhand der ID

    mail = MailSender()      # Verbindung zum Mail-Server erstellen

    # Absendung der Mail initiieren
    mail.SendMail(
        pReceiver=donRec.email, 
        pSubject=f"Sponsoranmeldung für {user.lastname}, {user.firstname}", 
        pIsAttachement=False, 
        pMailText=views.DonRecAuth(request=request, UserID=UserID, user=user, DonRecID=DonationId,DonRec=donRec), 
        pAttachement="")
    
    mail.CloseConnection()      # Verbindung zum Server abbrechen

    return HttpResponse(f"Mail send to {user.lastname}, {user.firstname}")       # Bekomme einzelnen Spendeneintrag anhand der ID


# Vorlage für ein Listen Objekt zum Speichern der 
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
        

# Binary Search für das Userobjekt
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
    donRec = donationrecord.objects.filter(email=DonRecEmail) # Ziehe alle Spendeneinträge mir der E-Mail

    set.logger.print(donRec)
    # Implementiere alle Variablen
    mail = None
    TotalDonation: float
    TotalDonation = 0
    TotalKilometers = 0
    data = []

    # Iteriere die Spendeneinträge, um Daten der Läufer zusammeln
    for val in donRec:
        usersIndex = BinarySearchUsers(users, val.iduser)
        Kilometers = users[usersIndex].kilometers
        # Erstelle den Daten eintrag
        dataRec = SponsData(
            pFirstname=users[usersIndex].firstname, 
            pLastname=users[usersIndex].lastname, 
            pKm=Kilometers, 
            pFixedDon=val.fixedamount, 
            pDon=val.donation)
        
        # Berechne die Kilometer Anzahl und Spendensumme aller Läufer des Sponsors
        TotalDonation += dataRec.DonationTotal
        TotalKilometers += Kilometers

        data.append(dataRec)

    # Lädt die generierten Daten in ein JSON Format
    context = {
            'name': f"{donRec[0].firstname} {donRec[0].lastname}",
            'Amount': len(donRec),
            'data': data,
            'Total': TotalDonation,
            'TotalKilometers': TotalKilometers,
        }

    set.logger.print(context)
    
    # Gibt die Daten, request und das Template  weiter -> erstellt den EMAIL inhalt
    return views.RenderMailText(context=context, request=request, template_name="SponsorInfo.html")




# Senden der Informationsmaails an alle Sponsoren
def sendSponsorInfo(request):
    users = Users.objects.order_by("iduser")        # Ziehe alle Nutzer, Sortiert nach der ID (für die Binary Search)

    # Ziehe jede E-Mail-Adr. einmal
    eMailArr = donationrecord.objects.values_list('email', flat=True).distinct()
    
    set.logger.print(users)

    mail = MailSender()     # Verbingung zum Mail-Server

    # Iteriert durch die gezogenen Mail-Adressen
    for eMail in eMailArr:
        mail.SendMail(
            pReceiver=eMail, 
            pSubject="Spendenlauf Spenden Informationen", 
            pIsAttachement=False, 
            pMailText=loadSponsorInfo(request=request, DonRecEmail=eMail, users=users),  # 
            pAttachement="")

    mail.CloseConnection()  # Schließe die Verbindung zu Server

    return HttpResponse("Mails send!")      # Gebe eine HTTP-Anwtwort







# Laden der Läufer Informations Mails
def loadRunnerInfo(request, donRecs, user, RunnerAmount, EventKilometers, EventTotal):
    # Variablen implementieren
    mail = None
    Kilometers = user.kilometers
    SponsorAmount = donRecs.filter(iduser=user.iduser).count()
    data = []
    RunnerTotal: float
    RunnerTotal = 0

    # Iterieren der Spendeneinträge mit nutzer id
    for val in donRecs.filter(iduser=user.iduser):
        # Erstellt die Einräge der Sponsor Daten
        dataRec = SponsData(
            pFirstname=val.firstname, 
            pLastname=val.lastname, 
            pKm=Kilometers, 
            pFixedDon=val.fixedamount, 
            pDon=val.donation)
        
        RunnerTotal += dataRec.DonationTotal        # Zählt die Läufer Spendeneinahmen
        
        data.append(dataRec)        # Übergibt den Spendeneintrag in die Liste

    # Laden der Daten in das JSON Format
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

    set.logger.print(context)
    # Gibt die Daten, request und das Template  weiter -> erstellt den EMAIL inhalt
    return views.RenderMailText(context=context, request=request, template_name="RunnerInfo.html")





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
    set.logger.print("test")
    # usersSortet = users.order_by("iduser")
    for donRec in donRecs.filter(verified=True):
        if donRec.fixedamount:
            EventTotal += donRec.donation
        else:
            set.logger.print(donRec.iduser)
            km = 0
            try:
                # set.logger.printLog("filter")
                # set.logger.printLog(users.filter(iduser=donRec.iduser)[0].kilometers)
                km = users.get(iduser=donRec.iduser).kilometers
            except Exception as es:
                set.logger.print("error ", es)

            EventTotal += donRec.donation * km

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


