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
#     "sender_email":"",
#     "password":""
# }
###########################################

df = pd.read_json('MailConfig.json', typ="series")

# Werte ausgeben
print(df.sender_email)  
print(df.password)  


#Read from customizing
smtp_server = ""
smtp_port = 0

matches = re.findall(r'"(.*?)"', line)   



translation_table = dict.fromkeys(map(ord, '"'), None) #Dont change

