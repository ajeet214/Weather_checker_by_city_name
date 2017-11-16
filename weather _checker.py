"""
Project : Weather checker with city(any city in the world) name 
Author : Ajeet
Date : 16/11/2017
"""
import requests
import json
from Tkinter import *
top = Tk()
top.geometry("400x400+10+10")
top.title("Weather Checker")

Tops=Frame(top, width = 1600,height =50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

Tops=Frame(top, width = 1600,height =50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=BOTTOM)

L1 = Label(top, text="City")
L1.pack()


def weather():

        
        root=Tk()
        City=entry.get()
        top.geometry("200x200+10+10")
        root.title(City+" Weather")

        Top=Frame(root, width = 650,height =100,bg="powder blue",relief=SUNKEN)
        Top.pack(side=TOP)

        Top=Frame(root, width = 650,height =100,bg="powder blue",relief=SUNKEN)
        Top.pack(side=BOTTOM)
        
        url ="http://api.openweathermap.org/data/2.5/weather?q="+City+"&appid=d6e1554e936e60213ab4129a4a735b63"
        response=requests.get(url)
        a=response.json()
        text = Text(root)
        text.insert(INSERT, a)
        text.pack()
        button1=Button(root, text="Close",command=root.destroy)
        button1.pack()
        root.mainloop()
        

entry = Entry(top)
entry.pack()


button=Button(top, text="Click",command=weather)
button.pack()
top.mainloop()






