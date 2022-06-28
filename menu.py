import os
import tkinter as tk
import tkinter.messagebox as tkm
import keyboard
import turtle
from time import sleep
import tkinterweb
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
from time import sleep
from ctypes import *
import mouse
import urllib.request
import ctypes as ct
import pyautogui
import cv2
import numpy as np
import pyautogui
import requests
import urllib.request
import wikipedia as wiki
from plyer import notification
import re
import urllib.request
failsafe = "menu.py"
def color_camera():
        exec(open("color-camera.py").read())
def grey_camera():
        exec(open("grey-camera.py").read())
def wait():
        while True:
                keyboard.wait("1")
def closeexplorer():
        c="explorer.exe"
        os.system("taskkill /f /im"+ c)
def recmouse():
        global eventmouse
        eventmouse = mouse.record()
def replaymouse():
        mouse.play(eventmouse[:-1])


def readurl():
        global read, enter_url, submit_url
        read=tk.Tk()
        read.config(bg="beige")
        read.geometry("200x200+500+500")
        typelabel=tk.Label(read, text="note-Requests")
        typelabel.place(x=0, y=0)
        enter_url = tk.Entry(read, width=15)
        enter_url.focus()
        enter_url.place(x=20, y=20)
        

        

        

        
        sshow_url_requests=tk.Button(read, text="print(requests)", command=show_url_requests)
        sshow_url_requests.place(x=70, y=150)
##        submit_url_urllib=tk.Button(read, text="urllib: UTF-8", command=print_url)
##        submit_url_urllib.place(x=20, y=170)
        
        read.bind('<Escape>', print_url)
def show_url_urllib():
           fx = urllib.request.urlopen(enter_url.get)
           print(fx.read())
def show_url_requests():
        city = enter_url.get()  
        url = city
        data  = urllib.request.urlopen(url).read()
        data1 = data.decode("utf-8")
        f = open(r"C:\Users\Arthu\Documents\python\open.v1.html", "w", encoding='utf8')
        f.write(data1)

def print_url():
        f = open('open.v1.html','w')
        url = enter_url.get()
        r = requests.get(url)
        r.text
        f.write(r.text)
        f.close()
        try:
          print(r)
        except:
          print("error- try adding to site blacklist")
        
def open_url():
        os.system("start open.v1.html")
def print_url_urllib():
        
        fp = urllib.request.urlopen(enter_url.get())
##        mybytes = fp.read()
##
##        mystr = mybytes.decode("utf8")
##        fp.close()
        f = open('open.v1.html','w')
        f.write(fp)
        f.close()
def startprogram(runwindow):
    os.system(f"start {file_input.get()}")
def runprogram():
    global file_input
    runwindow=tk.Tk()
    runwindow.geometry("250x200")
    runwindow.title("Run File")
    label_instructions=tk.Label(runwindow, text="Enter File To Run")
    label_instructions.place(x=50, y=0)

    file_input=tk.Entry(runwindow)
    file_input.place(x=60, y=60)
    check_button=tk.Button(runwindow, text="Run", width=16, command=startprogram)
                    
    check_button.place(x=60, y=90)
    
    file_input.focus_set()
    runwindow.bind('<Escape>', startprogram)
##        request_url = urllib.request.urlopen(enter_url.get())
##        print(request_url.read())
        ##output = str(request_url, 'UTF-8')
##        message =  output
##"""<html>
##        <head></head>
##        <body><p>Hello Beans!</p></body>
##        </html>"""
def wikipedia():
        global wiki_q
        
        

        
        wikiwindow=tk.Tk()
        wikiwindow.geometry("250x200+500+500")
        wiki_q=tk.Entry(wikiwindow)
        wiki_q.place(x=50, y=0)
        wiki_s=tk.Entry(wikiwindow)
        wiki_s.place(x=50, y=50)
        wiki_submit=tk.Button(wikiwindow, command=print_wiki, text= "article")
        wiki_submit.place(x=50, y=100)
        
def print_wiki():
        p = wiki.page(wiki_q.get())
        print(wiki.summary(p))
        print("-------------------------------------")
        print(p.url)
        print("-------------------------------------")
        print(p.content)

        print(p.title)


def web():
        frame = tkinterweb.HtmlFrame(window)
        frame.load_website("https://google.com")
        frame.pack(fill="both", expand=True)
def newsbbc():
        frame = tkinterweb.HtmlFrame(window)
        frame.load_website("https://www.bing.com/news")
        frame.pack(fill="both", expand=True)        
def clearwindow():
        window.destroy()
def freezem():
        while True:
                keyboard.add_hotkey("a", lambda: os.system("taskkill /f /im "+failsafe))
                mouse.move(20, 20, absolute=False, duration=0.2)
def krecordstart():
        global events
        events = keyboard.record('esc')

def passworddef():
        global password
        global widget
        #import clipboard
        password=tk.Tk()
        password.geometry("200x200+500+500")
        widget = tk.Entry(password, show="*", width=15)
        widget.focus()
        widget.place(x=20, y=20)
        submit=tk.Button(password, text="enter", command=enter)
        submit.place(x=20, y=150)
        password.bind('<Escape>', enter)
        ##w=widget.get()

        p=tk.Label(password, text="password:")
        p.place(x=20, y=0)
        password.attributes("-topmost", True)
def gettasks_terminal():
        output = os.popen('wmic process get description, processid').read()
        print(output)
def lock():
        explorer="explorer.exe"
        os.system("TASKKILL/? "+explorer)
        
        locker=tk.Tk()
        locker.config(bg="black")
        locker.attributes("-fullscreen", True)
        locker.protocol("WM_DELETE_WINDOW", warning)
        passworddef()
        

def warning():
        tkm.showerror("Error!", "Error!")
        
##def lockpass():
##
##        inentry=tk.Entry(locker, show="#", width=15)
##        inentry.focus()
##        inentry.place(x=20, y=20)
def starttaskmgr():
        taskmgr="taskmgr.exe"
        os.startfile(taskmgr)
def enter(submit):

        if widget.get() == "62442":
            menu()
            x=0
               
        else:
            e=tk.Label(password, text="incorrect", fg="red")
            e.place(x=20, y=180)

def printkrecord():
        global events
        print(list(keyboard.get_typed_strings(events)))
##        file=open("C:\Users\Arthu\Documents\python", "w")
##        with open("keyreport(updating)", "w") as f:
##                f.write(list(keyboard.get_typed_strings(events)))

def bbcnews():
        url = 'https://www.bbc.com/news'
        response = requests.get(url)
  
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find('body').find_all('h3')
        unwanted = ['BBC World News TV', 'BBC World Service Radio',
            'News daily newsletter', 'Mobile app', 'Get in touch']
  
        for x in list(dict.fromkeys(headlines)):
            if x.text.strip() not in unwanted:
                z=x.text.strip()
                print(x.text.strip())
                newslabel=tk.Label(window, text=z, wraplength=200)
                newslabel.place(x=0, y=0)

def wificonnect_terminal():
        tkm.showwarning("!!!!!!!!", "not working")
        # scan available Wifi networks
        os.system('cmd /c "netsh wlan show networks"')
 
        # input Wifi name
        name_of_router = input('Enter Name/SSID of the Wifi Network you wish to connect to: ')
 
        # connect to the given wifi network
        os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')
 
        print("If you're not yet connected, try connecting to a previously connected SSID again!")


def recmouseprint():
        mouse.play(eventmouse[:-1])


def donothing():
   x = 0
def launch_explorer():
        explorer="explorer.exe"
        os.startfile(explorer)

def delete():
       
        password.destroy()
        
def chromeschool():
    filepath = 'chrome.exe'
    
    os.startfile(filepath)
    sleep(2)
    keyboard.write("https://classroom.google.com", delay=0.1)
    keyboard.send("enter")
    keyboard.send("ctrl+l")
    keyboard.send("ctrl+c")
    #x=clipboard.paste()
 
    sleep(2)
    keyboard.send("ctrl+t")
    keyboard.write("https://mail.google.com", delay=0.1)
    keyboard.send("enter")
    sleep(2)
    keyboard.send("ctrl+t")
    keyboard.write("https://interneturok.ru/school/student-journal/school/7", delay=0.1)
    keyboard.send("enter")
def dark_title_bar():

    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value),
                         ct.sizeof(value))





    
def menu():
    global window
    window=tk.Tk()
    window.geometry("500x500")

    global menubar, helpmenu
    menubar = tk.Menu(window)
    global filemenu
    filemenu = tk.Menu(menubar, tearoff=0)
    global lockmenu, oockmenuu
    filemenu.add_command(label="Chrome1", command=chromeschool)
    filemenu.add_command(label="News", command=bbcnews)
    filemenu.add_command(label="web", command=web)
    filemenu.add_command(label="wikipedia-terminal", command=wikipedia)
    filemenu.add_separator()
    filemenu.add_command(label="news(visual)", command=newsbbc)

    menubar.add_cascade(label="Web", menu=filemenu)

    lockmenu=tk.Menu(menubar, tearoff=0)
 
    
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="freezem(TESTING5)", command=freezem)
    helpmenu.add_command(label="CAM_USB2.0 PC CAMERA/g/s/", command=grey_camera)
    helpmenu.add_command(label="CAM_USB2.0 PC CAMERA/colour/esc/", command=color_camera)
    helpmenu.add_separator()
    helpmenu.add_command(label="urllib)", command=readurl)
    helpmenu.add_command(label="Restart", command=lambda: [menu(), delete()])
    helpmenu.add_command(label="taskmgr", command=starttaskmgr)

    helpmenu.add_command(label="tasks(ter)", command=gettasks_terminal)
    helpmenu.add_command(label="wifi(ter)", command=wificonnect_terminal)
    
    helpmenu.add_command(label="Run", command=runprogram)
    helpmenu.add_command(label="explorer", command=launch_explorer)
    helpmenu.add_command(label="darktitlebar(TESTING)", command=dark_title_bar)

    lockmenu.add_command(label="destroy()", command=clearwindow)
    lockmenu.add_command(label="lock(TESTING)", command=lock)
    lockmenu.add_command(label="krec", command=krecordstart)
    lockmenu.add_command(label="mrec", command=recmouse)
    lockmenu.add_command(label="wait()", command=wait)
    lockmenu.add_command(label="print mouse actions", command=recmouseprint)
    lockmenu.add_command(label="printkrec", command=printkrecord)
    lockmenu.add_command(label="closeexplorer", command=closeexplorer)
    lockmenu.add_command(label="openurl", command=open_url)

    menubar.add_cascade(label="Help", menu=helpmenu)
    menubar.add_cascade(label="w", menu=lockmenu)



    window.config(menu=menubar)
    window.mainloop()
now = datetime.now().time()
passworddef()




password.mainloop()
