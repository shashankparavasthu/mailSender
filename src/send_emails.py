from tkinter import *
import config
import smtplib, ssl
from emailer import Email
import refactor
import update_display
import email_results


def send_emails(sender_username, password, subject, message, attachment, extension):
    # config.buttons[1].config(state='disabled')
    update_display.disable_all_input()

    sender_email = sender_username.get()
    user_password = password.get()
    email_subject = subject.get('1.0','end-1c')
    email_message = message.get('1.0','end-1c')
    attachment_regex = attachment.get()
    attachment_extension = extension.get()

    email_results.create_results_sheet()

    with smtplib.SMTP_SSL("smtp.gmail.com", config.port, context=config.context) as server:
        try:    
            # login with credentials
            server.login(sender_email, user_password)
            
            print("sending mails")
            #iterate over recipients list and send mail to each of them
            for recipient_number in config.recipients:

                #add recipient to email results
                email_results.add_cell_value(int(recipient_number), 1, config.recipients[recipient_number]["email"] + recipient_number)
                
                try:
                    personal_subject = refactor.refactor(recipient_number, email_subject)
                    personal_message = refactor.refactor(recipient_number, email_message)
                    attachment_value = refactor.refactor(recipient_number, attachment_regex)
                    attachment_value = attachment_value + attachment_extension
                    new_email = Email(sender_email, config.recipients[recipient_number]["email"], personal_subject, personal_message, attachment_value)
                    new_email.send_email(server)
                    
                    sent_message = str(recipient_number) + ". sent mail from " + sender_email + " to " + config.recipients[recipient_number]["email"]
                    update_display.update_display(sent_message)
                    email_results.add_cell_value(int(recipient_number), 2, sent_message)

                except Exception as e:
                    exception_message = str(e)
                    
                    update_display.update_display(exception_message)
                    email_results.add_cell_value(int(recipient_number), 2, exception_message)

                    continue
        
            #save workbook after sending all mails                    
            email_results.save_results()    
            update_display.update_display("Completed.")
                
        except Exception as e: 
            #save workbook after sending all mails                    
            email_results.save_results()    
            
            update_display.update_display(str(e))    
            pass    

                