#! /usr/bin/env python3
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Credentials
FROM_EMAIL = os.getenv("FROM_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")
PASSWORD = os.getenv("PASSWORD")

#Setup the MIME
message = MIMEMultipart()
message['From'] = FROM_EMAIL
message['To'] = TO_EMAIL
message['Subject'] = 'Dream Date Animal!'

#The body and the attachments for the mail
with open("tfanimal.txt") as dd_txt:
    text = dd_txt.read()
    message.attach(MIMEText(text, 'plain'))
    attach_file_name = 'tfanimal.txt'
    attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment
    #Add payload header with filename
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.ehlo()
    session.starttls() #enable security
    session.login(FROM_EMAIL, PASSWORD, initial_response_ok=True) #login with mail_id and password
    text = message.as_string()
    session.sendmail(FROM_EMAIL, TO_EMAIL, text)
    session.quit()
