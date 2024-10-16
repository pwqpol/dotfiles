import subprocess
import tkinter as tk
from tkinter import *
root = Tk()


def set_label():
    global label_text
    command = "xprop -root _NET_ACTIVE_WINDOW"
    frontmost = subprocess.check_output(["ksh", "-c", command]).decode("utf-8").strip().split()[-1]
    command1 = f'xprop WM_NAME -id {frontmost}'
    name = subprocess.check_output(["ksh", "-c", command1]).decode("utf-8")
    winname= name.split()[2]
    label_text = winname.replace('"', '')
    label.config(text=label_text )

while True
    if 

label = Label(root, text='')
label.pack(pady=5, padx=5)
set_label()
root.mainloop()
