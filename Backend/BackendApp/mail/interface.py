import smtplib
import csv
import re
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import json
import pandas as pd



###########Create Mail Interface############
# Create the file 'MailConfig.json' in this folder
# set the values sender_email and password. Like
# {
#     "sender_email":"test@test.de",
#     "password":"password123"
#     "smtp_Server":"smtp.gmail.com",
#     "smtp_Port":587
# }
# the smtp_port should be an integer
###########################################
# Werte ausgeben

#Read from customizing
# global ServerData
# _ServerData = pd.read_json('MailConfig.json', typ="series")

# print(_ServerData)
# matches = re.findall(r'"(.*?)"', line)   

class getServerData:
    sender_mail: str
    password: str
    smtp_server: str
    smtp_port: int
    def __init__(self):
        _getData = pd.read_json('MailConfig.json', typ="series")
        self.sender_mail = _getData.sender_mail
        self.password = _getData.password
        self.smtp_server = _getData.smtp_server
        self.smtp_port = _getData.smtp_port 
        
# translation_table = dict.fromkeys(map(ord, '"'), None) #Dont change

class MailSender():
    Server = None
    SD = None

    def __init__(self):
        self.SD = getServerData()
        print(self.SD)
        print(self.SD.sender_mail)
        self.ConnectToServer()

    def ConnectToServer(self):
        print(self.SD.smtp_server)
        self.Server = smtplib.SMTP(self.SD.smtp_server, self.SD.smtp_port)
        self.Server.starttls()
        self.Server.login(self.SD.sender_email, self.SD.password)
        print("Connection to Mail-Server successfuly")

    def SendMail(self, pReceiver: str, pSubject: str, pIsAttachement: bool, pAttachement, pMailText: str):
        msg = MIMEMultipart()
        msg['Subject'] = pSubject
        msg['From'] = self.SD.sender_mail
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

        print(msg.as_string())
        Waiter = input("Waiting")
        encoders.encode_base64(part)
        
        part.add_header('Content-Disposition', 'attachment; filename="Example_doc.pdf"')


        msg.attach(part)

        try:
            self.Server.sendmail(self.SD.sender_email, pReceiver, msg.as_string())#"Subject: \n\n This is definitly not a Virus. Trust me bro: http://localhost:3000/register")
        except:
            print("Unexpected error ocurred while sending Mail!")
        
    # def generate

    def CloseConnection(self):
        self.Server.quit()
    


mail = MailSender()
mail.SendMail(pReceiver="jesper@herlings.de", pSubject="tset", pIsAttachement=False, pMailText="Hello", pAttachement="")