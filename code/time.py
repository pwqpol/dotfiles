#!/usr/local/bin/python3

from datetime import datetime
import tkinter as tk
from tkinter import *


def label_text():
    time_n = datetime.now().strftime(' %H:%M ')
    date_n = datetime.now().strftime(' %d-%m-%Y ')
    label_time.configure(text=time_n)
    label_date.configure(text=date_n)

root = Tk()
root.geometry("150x100-4+3")
root.resizable(0, 0)
root.config(bg="#282828")

label_time = Label(root, text="", font=("ubuntu", 30), bg="#282828", fg="#ebdbb2")
label_time.pack()
label_date = Label(root, text="", font=("ubuntu", 20), bg="#282828", fg="#ebdbb2")
label_date.pack()

label_text()
root.after(4000, root.destroy  )
root.mainloop()
