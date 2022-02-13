import config
import tkinter as tk
from tkinter import *

def update_display(text):
    # text = text + config.display_var.get() + "\n"
    config.display_text.config(state = NORMAL)
    config.display_text.insert(END, "\n" + text) 
    config.display_text.config(state = DISABLED)
    config.input_window.update()

def disable_all_input():
    for widget in config.widgets:
        widget.config(state='disabled')

def update_label(label, text):
    label.set(text)