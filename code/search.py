import tkinter as tk
from tkinter import *
import webbrowser




root = Tk()
root.config(bg="#282828")
root.geometry("800x60")
root.update_idletasks()	
windowWidth = root.winfo_width()
windowHeight = root.winfo_height()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2 - 200)
root.geometry("+{}+{}".format(positionRight, positionDown))


def get_string():
    string = entry.get()
    a = string.split()
    b = "+".join(a)
    root.destroy()
    webbrowser.open(f'https://duckduckgo.com/lite/search?q={b}')    
entry = Entry(root, bg="grey", fg="#ebdbb2", font=("ubuntu", 12), width=70)
entry.pack(pady=3, padx=3, fill="x")
entry.focus()
button1 = Button(root, text="search", bg="#282828", fg="#ebdbb2", font=("ubuntu", 10), command=get_string, activebackground="#262626", activeforeground="orange", width=30)
button1.pack(pady=3, padx=3)

root.mainloop()
