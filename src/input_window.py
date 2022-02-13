import tkinter as tk
from tkinter import *
import config
import send_emails

def create_ui():
    input_window = tk.Tk()
    input_window.title("Garuda")

    config.init_widgets()

    input_window.grid_columnconfigure(1, weight=1)

    input_box_column = 1
    label_column = 0

    #sender email
    sender_label = Label(input_window, text = 'Sender Email')
    sender_label.grid(row = 0, column = label_column, sticky = tk.W)
    sender_box  = Entry(input_window)
    sender_box.grid(row = 0, column = input_box_column, sticky = tk.W + tk.E)
    config.add_widget(sender_box)

    #password
    password = Label(input_window, text = 'password') 
    password.grid(row =1, column = label_column, sticky = tk.W)
    password_box  = Entry(input_window) # add show = '*' to hide password on screen 
    password_box.grid(row = 1,column = input_box_column,  sticky = tk.W + tk.E)
    config.add_widget(password_box)

    #subject
    subject = Label(input_window, text = 'subject') 
    subject.grid(row = 2, column = label_column, sticky = tk.W)
    subject_box = Text(input_window, height = 2)
    subject_box.grid(row = 2, column = input_box_column)
    config.add_widget(subject_box)

    #message
    message = Label(input_window, text = 'message') 
    message.grid(row = 3, column = label_column, sticky = tk.W)
    message_box = Text(input_window, height = 10)
    message_box.grid(row = 3, column = input_box_column)
    config.add_widget(message_box)

    #mailing list
    input_window.columnconfigure(4, weight=0)
    mail_list = Label(input_window, text = 'Add Receivers List')
    mail_list.grid(row = 4, column = label_column, sticky = tk.W)
    
    mail_list_file = tk.StringVar(input_window)
    mail_list_file.set("No File Chosen")
    mail_list_label = Label(input_window, textvariable = mail_list_file)
    

    mail_list_button = Button(input_window, text = "Browse Local", command = lambda: config.init_recipients(
        mail_list_file))
    mail_list_button.grid(row = 4, column = input_box_column, sticky = tk.W + tk.E) 
   
    mail_list_label.grid(row = 4, column = input_box_column + 1, sticky = tk.W)
    
    config.add_widget(mail_list_button)
    
    #attachment
    attachment = Label(input_window, text = 'Attachment Regex')
    attachment.grid(row = 5, column = label_column, sticky = tk.W)
    attachment_box = Entry(input_window, width = 2)
    attachment_box.grid(row = 5, column = input_box_column, sticky = tk.W + tk.E)
    config.add_widget(attachment_box)

    #attachment_extension
    extension_value = tk.StringVar(input_window)
    extension_value.set(config.extensions[0])

    extension = tk.OptionMenu(input_window, extension_value, *config.extensions)
    extension.grid(row = 5, column = input_box_column + 1)
    config.add_widget(extension)

    #attachment folder
    attachment_folder_label = Label(input_window, text = 'Attachment Folder')
    attachment_folder_label.grid(row = 6, column = label_column, sticky = tk.W)

    attachment_folder = tk.StringVar(input_window)
    attachment_folder.set("No File Chosen")
    attachment_folder_label = Label(input_window, textvariable = attachment_folder)

    attachment_folder_button = Button(input_window, text = "Browse Local", command = lambda: config.set_attachment_folder(attachment_folder))
    attachment_folder_button.grid(row = 6, column = input_box_column, sticky = tk.W + tk.E) 

    attachment_folder_label.grid(row = 6, column = input_box_column + 1, sticky = tk.W)

    config.add_widget(attachment_folder_button)

    #send mails
    send_button = Button(input_window, text= 'Send Emails', 
                            command = lambda: send_emails.send_emails(sender_box, password_box
                            , subject_box, message_box, attachment_box, extension_value))
    send_button.grid(column =input_box_column, sticky = tk.W)
    config.add_widget(send_button)

    #displayText
    display_text =Text(input_window, state = DISABLED, height = 20, bg = "gray77")
    display_text.grid(column =input_box_column, sticky = tk.W)

    config.init_display(display_text)
    config.init_input_screen(input_window)

    #enable scroll for displayText
    scroll_bar = tk.Scrollbar(input_window)
    display_text.config(yscrollcommand=scroll_bar.set)
    display_text.config(xscrollcommand=scroll_bar.set)

    return input_window
