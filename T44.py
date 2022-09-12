import webbrowser
from tkinter import *


window = Tk()
window.geometry("500x500")
window.title("Web Browser")

Label(window,text="Favorite Web Pages",font=("Helvtica 25 bold")).pack()
Label(window,text="Click  On button to Open  Webpge",font="Tahoma").pack()

def whatsapp_web():
    webbrowser.open("https://web.whatsapp.com/")

def Telegram_web():
    webbrowser.open("https://desktop.telegram.org/")

def instagram_web():
    webbrowser.open("https://www.instagram.com/")

def gmail():
    webbrowser.open("www.Gmail.com")





telegram = Button(window,text="Telegram Web",relief="ridge",bd=6,bg="blue",fg="white",font=("calibri 15 bold"),command=Telegram_web ).pack(padx=20,pady=20)
whatsapp = Button(window,text="Whatsapp Web",fg="white",activeforeground="red",bg="green",font=("tahoma 10 bold"),command=whatsapp_web ).pack(padx=20,pady=20)
instagram = Button(window,text="instagram Web",bd=5,relief="sunken",bg="white",fg="purple",font=("Digital 10 bold"),command=instagram_web ).pack(padx=20,pady=20)
g = Button(window,text="Gmail",bg="red",fg="yellow",font=("clasic 10 italic bold"),relief="groov",activeforeground="blue",bd=4,command=gmail ).pack(padx=20,pady=20)


window.mainloop()