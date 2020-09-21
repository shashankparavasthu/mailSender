import tkinter as tk
from tkinter import *
import config
import send_emails

def create_ui():
    input_window = tk.Tk()
    input_window.title("Garuda")

    config.init_buttons()

    input_box_column = 1
    label_column = 0

    #sender email
    sender_label = Label(input_window, text = 'Sender Email')
    sender_label.grid(row = 0, column = label_column, sticky = tk.W)
    sender_box  = Entry(input_window)
    sender_box.grid(row = 0, column = input_box_column, sticky = tk.W + tk.E)

    #password
    password = Label(input_window, text = 'password') 
    password.grid(row =1, column = label_column, sticky = tk.W)
    password_box  = Entry(input_window) # add show = '*' to hide password on screen 
    password_box.grid(row = 1,column = input_box_column,  sticky = tk.W + tk.E)

    #subject
    subject = Label(input_window, text = 'subject') 
    subject.grid(row = 2, column = label_column, sticky = tk.W)
    subject_box = Text(input_window, height = 2)
    subject_box.grid(row = 2, column = input_box_column)
        
    #message
    message = Label(input_window, text = 'message') 
    message.grid(row = 3, column = label_column, sticky = tk.W)
    message_box = Text(input_window, height = 10)
    message_box.grid(row = 3, column = input_box_column)

    #mailing list
    mail_list = Label(input_window, text = 'Add Receivers List')
    mail_list.grid(row = 4, column = label_column, sticky = tk.W)
    mail_list_button = Button(input_window, text = "Browse Local", command = config.init_recipients)
    mail_list_button.grid(row = 4, column = input_box_column, sticky = tk.W) 
    config.add_buttons(mail_list_button)

    #attachment
    attachment = Label(input_window, text = 'Attachment Regex')
    attachment.grid(row = 5, column = label_column, sticky = tk.W)
    attachment_box = Entry(input_window, width = 2)
    attachment_box.grid(row = 5, column = input_box_column, columnspan = 2, sticky = tk.W + tk.E)

    #attachment_extension
    extension_value = tk.StringVar(input_window)
    extension_value.set(config.extensions[0])

    extension = tk.OptionMenu(input_window, extension_value, *config.extensions)
    extension.grid(row = 5, column = input_box_column + 1)

    #attachment folder
    attachment_folder_label = Label(input_window, text = 'Attachment Folder')
    attachment_folder_label.grid(row = 6, column = label_column, sticky = tk.W)
    attachment_folder_button = Button(input_window, text = "Browse Local", command = config.set_attachment_folder)
    attachment_folder_button.grid(row = 6, column = input_box_column, sticky = tk.W) 
    config.add_buttons(attachment_folder_button)

    #send mails
    send_button = Button(input_window, text= 'Send Emails', 
                            command = lambda: send_emails.send_emails(sender_box, password_box
                            , subject_box, message_box, attachment_box, extension_value))
    send_button.grid(column =input_box_column, sticky = tk.W)
    config.add_buttons(send_button)

    return input_window
