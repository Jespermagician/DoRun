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
from BackendApp.settings import logger

##########################################################################
# please read in the doku, how to set up the mail server connection !!!!!#
##########################################################################

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
        

# Main class which handles the main 
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

    def SendMail(self, pReceiver: str, pSubject: str, pMailText: str, pPlainText: str, pAttachement=None):
        msg = MIMEMultipart()                               # Erstellt eine  Nachricht 
        msg['Subject'] = pSubject                           # Betreff
        msg['From'] = self.SD.sender_email                  # Absenderadresse
        msg['To'] = pReceiver                               # Empfängeradresse
        
        # HTML-Version
        msg.attach(MIMEText(pMailText, 'html', 'utf-8'))    # Fügt den HTML-Nachrichtentext hinzu
        
        # Text-Version
        # msg.attach(MIMEText(pPlainText, 'plain', 'utf-8'))  
        
        # Überprüfen, ob Anhänge gesetzt sind
        if pAttachement != None:
            logger.print("There is an attachment set. But no action will follow!")

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


###########Create Mail Interface############
# Create the file 'MailConfig.json' in the CustomData folder
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
