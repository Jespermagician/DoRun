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
# Please refer to the documentation on how to set up the mail server connection!
##########################################################################

class getServerData:
    sender_email: str
    password: str
    smtp_server: str
    smtp_port: int

    def __init__(self):
        _getData = pd.read_json(f"{views.BASE_DIR}\\Backend\\CustomData\\MailConfig.json", typ="series")
        set.logger.print(_getData)
        # The attribute names in _getData must match those in the JSON file
        self.sender_email = _getData.sender_email
        self.password = _getData.password
        self.smtp_server = _getData.smtp_server
        self.smtp_port = _getData.smtp_port 


# Main class that handles mail operations
class MailSender():
    Server = None  # SMTP connection to the mail server
    SD = None      # Object containing server data like host, port, and login credentials

    def __init__(self): 
        self.SD = getServerData()  # Function to fetch server configuration (defined above)
        self.ConnectToServer()
        set.logger.print("Server Started")

    def ConnectToServer(self):  # Establishes connection to the SMTP server
        self.Server = smtplib.SMTP(host=self.SD.smtp_server, port=self.SD.smtp_port)
        self.Server.starttls()  # Enables TLS encryption
        self.Server.login(user=self.SD.sender_email, password=self.SD.password)  # Authentication

    def SendMail(self, pReceiver: str, pSubject: str, pMailText: str, pPlainText: str, pAttachement=None):
        msg = MIMEMultipart()  # Create an email message
        msg['Subject'] = pSubject            # Subject line
        msg['From'] = self.SD.sender_email   # Sender address
        msg['To'] = pReceiver                # Recipient address
        
        # HTML version of the email
        msg.attach(MIMEText(pMailText, 'html', 'utf-8'))  # Attach HTML content
        
        # Plain text version (currently disabled)
        # msg.attach(MIMEText(pPlainText, 'plain', 'utf-8'))  

        # Check if attachment is set
        if pAttachement is not None:
            logger.print("There is an attachment set. But no action will follow!")

        # Send the composed email
        try:
            self.Server.sendmail(self.SD.sender_email, pReceiver, msg.as_string())  # Send the email
            set.logger.print("Mail sent")  # Success message
        except:
            set.logger.print("Unexpected error occurred while sending Mail!")  # Error handling

    # Terminates the connection to the mail server
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
