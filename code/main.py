import tkinter as tk
from tkinter import *

root = Tk()
root.configure(bg="#282828")

def back():
    openbsd.destroy()
    root.deiconify()
def openbsd_window():
    global openbsd 
    root.withdraw()
    openbsd = Toplevel(root)
    openbsd.geometry("500x500")
    Label(openbsd, text="OpenBSD").pack()
    Button(openbsd, text="BACK", command=back).pack()
    



frame = LabelFrame(root, text="Main configuration", bg="#282828", fg="#ebdbb2", font=("ubuntu", 12))
frame.pack(pady=10, padx=10)

button1 = Button(frame, text="OpenBSD", bg="#282828", fg="#ebdbb2", font=("ubuntu", 12), width=15, highlightbackground="orange", relief="ridge", activebackground="#262626", activeforeground="orange", command=openbsd_window)
button1.pack(pady=10, padx=10)
button2 = Button(frame, text="Debian", bg="#282828", fg="#ebdbb2", font=("ubuntu", 12), width=15)
button2.pack(pady=10, padx=10)
button3 = Button(frame, text="NetBSD", bg="#282828", fg="#ebdbb2", font=("ubuntu", 12), width=15)
button3.pack(pady=10, padx=10)
button4 = Button(frame, text="Arch", bg="#282828", fg="#ebdbb2", font=("ubuntu", 12), width=15)
button4.pack(pady=10, padx=10)

button5 = Button(frame, text="EXIT", bg="#282828", fg="#ebdbb2", font=("ubuntu", 10), width=10, command=root.destroy)
button5.pack(pady=10, padx=10)


root.mainloop()
