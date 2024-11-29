import smtplib
import csv
import re
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import json
import pandas as pd
from . import views
from django.http import HttpResponse
from api.models import Users



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
def do(request, UserID):

    print(views.BASE_DIR)
    print(UserID)
    _getData = pd.read_json(f"{views.BASE_DIR}\Backend\CustomData\MailConfig.json", typ="series")
    print(_getData)

    UserModel = Users.objects.raw("Select * From api_users Where iduser = %s", [UserID])
    print(UserModel)
    mail: str
    for val in UserModel:
        mail = val.mail

    # print("test")
    # print(views.UserAuth(request, "Jesper Herling"))
    # test = input("i")clea

    mail = MailSender()
    mail.SendMail(
        pReceiver=mail, 
        pSubject="Anmeldung Spendenlauf", pIsAttachement=False, 
        pMailText=views.UserAuth(request=request, UserID=UserID), 
        pAttachement="")

    return HttpResponse("Mail send to Username")