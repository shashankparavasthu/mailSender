from tkinter import *
import config
import smtplib, ssl
from emailer import Email
import refactor

def send_emails(sender_username, password, subject, message, attachment, extension):
    config.buttons[1].config(state='disabled')

    sender_email = sender_username.get()
    user_password = password.get()
    email_subject = subject.get('1.0','end-1c')
    email_message = message.get('1.0','end-1c')
    attachment_regex = attachment.get()
    attachment_extension = extension.get()

    with smtplib.SMTP_SSL("smtp.gmail.com", config.port, context=config.context) as server:
        # login with credentials
        server.login(sender_email, user_password)
        
        #iterate over recipients list and send mail to each of them
        for recipient in config.recipients:
            personal_subject = refactor.refactor(recipient, email_subject)
            personal_message = refactor.refactor(recipient, email_message)
            attachment_value = refactor.refactor(recipient, attachment_regex)
            attachment_value = attachment_value + attachment_extension
            new_email = Email(sender_email, recipient, personal_subject, personal_message, attachment_value)
            new_email.send_email(server)
        

                