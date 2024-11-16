import smtplib
import csv
import re
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

Subject_File = "D:\Coding\Python\DoRun\E-Mail Texts\Subjects.csv"
Mailbody_File = "D:\Coding\Python\DoRun\E-Mail Texts\Mailbody.csv"
attachement = "D:\Coding\Python\DoRun\E-Mail Texts\Example_doc.pdf"
customizing_file = "D:\Coding\Python\DoRun\E-Mail Texts\Customizing.txt"

rec_email = "weiershausenf@gmail.com"

#Read from customizing
sender_email = ""#"DoRun.NoReply@gmail.com"
password = ""#"ctvv dslc gvaf frku " #input(str("Enter Password: ")) Gmail requires a app-password for each client that is allowed to send mails

#Read from customizing
smtp_server = ""
smtp_port = 0

translation_table = dict.fromkeys(map(ord, '"'), None) #Dont change

def GetText(SType,Filepath):
    # Get Subject
    Text = "Error"
    #Open csv file 
    with open(Filepath, mode= 'r', newline='', encoding='utf-8') as file:
        Textreader = csv.reader(file, delimiter='_', quotechar='|', skipinitialspace= True)

        #Read each row of the csv file to find the text behind the SType
        for row in Textreader:
            a = (', '.join(row))
                    
            #If SType matches index/key in csv file get the text
            if (int(a[0]) == int(SType)):
                print(a)
                a = a.translate(translation_table) #replaces " with none so you can , in the csv 
                substring = a.split(",", 1)
                #print(substring)
                Text = substring[1]
                exit
    return Text
    
if __name__ == "__main__":
    
    SType = int(input(str("Geben sie die ID für den E-Mail typen an: ")))
    MailTexts = []
    Mailbody = ""
    
    #Read customizing
    f = open(customizing_file, "r")
    lines = f.readlines()

    i = 0
    for line in lines:
        matches = re.findall(r'"(.*?)"', line)   
        if matches:
            i = i + 1    
            match i:
                case 1:
                    sender_email = str(matches[0])
                case 2:
                    password = str(matches[0])
                case 3:
                    smtp_server = str(matches[0])
                case 4:
                    smtp_port = int(matches[0])
                case 5:
                    if (SType == 1):
                        for item in matches:
                            if item.strip():
                                cleaned_item = item.replace('[', '').replace(']', '')
                                MailTexts.extend([int(x) for x in cleaned_item.split(',')])
                case 6:
                    if (SType == 2):
                        for item in matches:
                            if item.strip():
                                cleaned_item = item.replace('[', '').replace(']', '')
                                MailTexts.extend([int(x) for x in cleaned_item.split(',')])                        
                case 7:
                    if (SType == 3):
                        for item in matches:
                            if item.strip():
                                cleaned_item = item.replace('[', '').replace(']', '')
                                MailTexts.extend([int(x) for x in cleaned_item.split(',')])                        
    
    #Start Mail processing
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, password)
    print("Login success")

    msg = MIMEMultipart()
    msg['Subject'] = GetText(SType, Subject_File)
    msg['From'] = sender_email
    msg['To'] = rec_email
    
    #Get Messagebody
    for i in MailTexts:
        MailTxt = str(GetText(i, Mailbody_File))
        Mailbody += MailTxt
    
    print(Mailbody)
    msg.attach(MIMEText(Mailbody, 'html', 'utf-8'))
    
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(attachement, "rb").read())
    print(msg.as_string())
    Waiter = input("Waiting")
    encoders.encode_base64(part)
    
    part.add_header('Content-Disposition', 'attachment; filename="Example_doc.pdf"')

    msg.attach(part)
    
    try:
        server.sendmail(sender_email, rec_email, msg.as_string())#"Subject: \n\n This is definitly not a Virus. Trust me bro: http://localhost:3000/register")
        server.quit()
        
    except:
        print("Unexpected error ocurred while sending Mail!")
    # end try

    a = input(str("Wait"))