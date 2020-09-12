import tkinter as tk
from tkinter import *
import config
import send_emails

def create_ui():
    input_window = tk.Tk()

    config.init_buttons()

    input_box_column = 8
    label_column = 0

    #sender email
    sender_label = Label(input_window, text = 'Sender Email')
    sender_label.grid(row = 0, column = label_column, sticky = tk.W)
    sender_box  = Entry(input_window)
    sender_box.grid(row = 0, column = input_box_column, sticky = tk.W)

    #password
    password = Label(input_window, text = 'password') 
    password.grid(row = 2, column = label_column, sticky = tk.W)
    password_box  = Entry(input_window) # add show = '*' to hide password on screen 
    password_box.grid(row = 2, column = input_box_column, sticky = tk.W)

    #subject
    subject = Label(input_window, text = 'subject') 
    subject.grid(row = 4, column = label_column, sticky = tk.W)
    subject_box = Text(input_window, height = 2)
    subject_box.grid(row = 4, column = input_box_column, sticky = tk.W)
        
    #message
    message = Label(input_window, text = 'message') 
    message.grid(row = 6, column = label_column, sticky = tk.W)
    message_box = Text(input_window, height = 10)
    message_box.grid(row = 6, column = input_box_column, sticky = tk.W)

    #mailing list
    mail_list = Label(input_window, text = 'Add Receivers List')
    mail_list.grid(row = 8, column = label_column, sticky = tk.W)
    mail_list_button = Button(input_window, text = "Browse Local", command = config.init_recipients)
    mail_list_button.grid(row = 8, column = input_box_column, sticky = tk.W) 
    config.add_buttons(mail_list_button)

    #send mails
    send_button = Button(input_window, text= 'Send Emails', 
                            command = lambda: send_emails.send_emails(sender_box, password_box
                            , subject_box, message_box))
    send_button.grid(row = 20, column =input_box_column, sticky = tk.W)
    config.add_buttons(send_button)

    return input_window
