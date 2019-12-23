# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 01:24:31 2019

@author: Gautam Pala
"""# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 00:51:11 2019

@author: Gautam Pala
"""

import tkinter as tk
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
from gtts import gTTS 
import os
import threading
import time

global text
global URL
global j
l2=[]
URL=input("please enter the Url of your form : ")
def fun1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            l2.append(text)
            print("You said : {}".format(text))
            
        except:
                print("Sorry could not recognize what you said")
                #return "Sorry could not recognize what you said"
def fun2(j):
        text = "please enter the " + l[j] 
        language = 'en'
        speech = gTTS(text = text, lang = language, slow = False)
        speech.save("text"+str(j)+".mp3")
        os.system("start text"+str(j)+".mp3")
        j=j+1           

#def fun3():
#    URL=e1.get()
    
#master=tk.Tk()         
#k.Label(master, text='Enter the URL for form').grid(row=0)
#e1 = tk.Entry(master)
#B0 = tk.Button(master, text="Submit", command=fun3,width=20  ,height=3, activebackground = "Blue" ,font=('times', 15, ' bold '))
#B0.place(x=100, y=300)
#URL=e1.get()
#URL = URL[1:len(URL)-1]
#e1.grid(row=0, column=1)
#B1 = tk.Button(master, text="Start", command=fun1,width=20  ,height=3, activebackground = "Blue" ,font=('times', 15, ' bold '))
#B1.place(x=200, y=500)
#B2 = tk.Button(master, text="Close", command=master.destroy,width=20  ,height=3, activebackground = "Blue" ,font=('times', 15, ' bold '))
#B2.place(x=600, y=500)
#URL = 'https://form.jotform.me/93325521458458' 
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
ip =soup.find_all("input")
label = soup.find_all("label")
print("-------------------------------")
l = []
for i in ip:
    if i["type"] != "hidden" and i["name"] != "website":
        for j in label:
            if i["id"] == j["for"]:
                l.append(j.text)
                break
print(l)
j=0
for i in range(len(l)):
        #time.sleep(2)
        threading.Thread(target=fun2(j)).start()
        time.sleep(5)
        threading.Thread(target=fun1()).start()
        j=j+1

    
print(l2)
print(URL)
time.sleep(2)
master=tk.Tk()

text=tk.Label(master,text=l[0]).grid(row=0)
e1=tk.Entry(master)
e1.insert(20,l2[0])
e1.grid(row=0,column=1)
text1=tk.Label(master,text=l[1]).grid(row=1)
e2=tk.Entry(master)
e2.insert(20,l2[1])
e2.grid(row=1,column=1)
text2=tk.Label(master,text=l[2]).grid(row=2)
e3=tk.Entry(master)
e3.insert(20,l2[2])
e3.grid(row=3,column=1)
master.mainloop()

     