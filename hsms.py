from tkinter import *       
from PIL import Image,ImageTk
win=Tk()
win.geometry("500x500")
win.resizable(0,0)
win.title("magical calcultor")
win.config(background="blue")
logo=PhotoImage(file="C:\\Users\\LENOVO\\Desktop\\hubnet.png")
win.iconphoto(0,logo)
e1=Entry(win,bg="white",fg="red",bd=15,font=("algerian",22,"bold"))
e1.pack()
win.mainloop()