from tkinter import *
import config
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import update_display

class Email:
    def __init__(self,sender_username, recipient_username, subject, message, attachment):
        self.sender_username =  sender_username
        self.recipient_username = recipient_username
        self.subject = subject
        self.message = message
        self.attachment = attachment
    
    def send_email(self, server):
        #send mail to individual receiver

        message_body = MIMEText(self.message, "plain")

        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = self.sender_username
        message["To"] = self.recipient_username
        message.attach(message_body)

        file_attachment = self.add_attachment()
        message.attach(file_attachment)

        #send mail
        server.sendmail(self.sender_username, self.recipient_username, message.as_string())
        

    def add_attachment(self):

        filename = config.attachment_folder + "/" + self.attachment

        # Open attachment file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            file_attachment = MIMEBase("application", "octet-stream")
            file_attachment.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(file_attachment)

        # Add header as key/value pair to attachment part
        file_attachment.add_header(
            'Content-Disposition', 'attachment', filename= self.attachment
        )

        return file_attachment