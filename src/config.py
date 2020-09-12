from tkinter import filedialog
import email, smtplib, ssl
from openpyxl import load_workbook
import json 

port = 465
context = ssl.create_default_context()

def init_recipients():
    global excel_file_path
    global recipients

    excel_file_path = filedialog.askopenfilename(title="select excel file:")

    workbook = load_workbook(filename = excel_file_path)
    sheet = workbook.active

    recipients = {}
    for value in sheet.iter_rows(min_row=1, max_row=1, values_only=True):
        col_names = value

    for value in sheet.iter_rows(min_row=2, values_only=True):
        new_mail = {}
        for i in range(1,len(value)):
            new_mail[col_names[i]] = value[i]
        recipients[value[0]] = new_mail
    
    print(json.dumps(recipients))


def init_buttons():
    global buttons 
    buttons = []

def add_buttons(button):
    buttons.append(button)
