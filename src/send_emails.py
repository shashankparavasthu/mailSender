from tkinter import *
import config
import smtplib, ssl
from emailer import Email
import refactor

def send_emails(sender_username, password, subject, message):
    config.buttons[1].config(state='disabled')

    sender_email = sender_username.get()
    user_password = password.get()
    email_subject = subject.get('1.0','end-1c')
    email_message = message.get('1.0','end-1c')

    with smtplib.SMTP_SSL("smtp.gmail.com", config.port, context=config.context) as server:
        #login with credentials
        server.login(sender_email, user_password)
        
        #iterate over recipients list and send mail to each of them
        for recipient in config.recipients:
            email_subject = refactor.refactor(recipient, email_subject)
            email_message = refactor.refactor(recipient, email_message)            
            new_email = Email(sender_email, recipient, email_subject, email_message)
            new_email.send_email(server)
        

                