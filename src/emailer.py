from tkinter import *
from config import * 
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email:
    def __init__(self,sender_username, recipient_username, subject, message):
        self.sender_username =  sender_username
        self.recipient_username = recipient_username
        self.subject = subject
        self.message = message
    
    def send_email(self, server):
        #send mail to individual receiver

        message_body = MIMEText(self.message, "plain")

        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = self.sender_username
        message["To"] = self.recipient_username
        message.attach(message_body)

        #send mail
        server.sendmail(self.sender_username, self.recipient_username, message.as_string())
        print(self.sender_username)
        print(self.recipient_username)
        print("sent mail to ", self.recipient_username)
