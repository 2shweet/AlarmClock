import tkinter as tk
from tkinter import *
import datetime
from bs4 import BeautifulSoup
import pyttsx3
import requests
from time import strftime



engine = pyttsx3.init()

mainWindow = tk.Tk()
mainWindow.title('ALARM CLOCK')

# setting up the time
def time():
    todayTime = datetime.datetime.now().strftime('%I:%M:%S %p')
    timeLabel.config(text=todayTime)
    timeLabel.after(1000, time)
timeLabel = tk.Label(mainWindow, font=('calibri', 40, 'bold'), background ='Green', foreground='white')
timeLabel.grid(row=0, column=0)

# Setting up speech for alarm clock
def speak(audio):
    engine.setProperty('rate', 170)  # setting up new voice rate you can adjust i find 170 most human like
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 1 for female 0 for male
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

def Weather():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
    url = requests.get('https://www.yahoo.com/news/weather/australia/sydney/sydney-1105779', headers=headers)
    soup = BeautifulSoup(url.content, 'html.parser')
    name = soup.find("div", {'class': "BdB Bds(d) Bdbc(#fff.12) Fz(1.2em) Py(2px) O(0) Pos(r) forecast-item Cur(p)"})
    speak(name)

# Gets the Latest world News from yahoo
def WorldNews():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
    url = requests.get('https://news.yahoo.com/world/', headers=headers)
    soup = BeautifulSoup(url.content, 'html.parser')
    name = soup.find("div", {'id': "mrt-node-YDC-Stream"})
    speak(name)

# setting up the alarm
def Alarm():
    alarmTime = f'{Hour.get()}:{minutes.get()}:{datetime.datetime.now().strftime("%S PM")}'
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    print(alarmTime)
    print(current_time)
    timeLabel.config(text=current_time)
    timeLabel.after(1000, Alarm)
    while True:
        if alarmTime == current_time:
            speak(f'Good Morning The Current time is {current_time}')
            speak('The Weather Today is Looking')
            Weather()
            speak('In World News Today')
            WorldNews()
        if current_time >= alarmTime:
            break
        return SetAlarm

# Creating the GUI for the alarm     
Hour = tk.StringVar(mainWindow)
minutes = tk.StringVar(mainWindow)

# Setting Up the Hour for Alarm
HourSet = tk.Label(mainWindow, text='HOURS').grid(row=1, column=0, sticky='nw', padx=20)
HourSetEntry = tk.Entry(mainWindow, width=25, textvariable=Hour).grid(row=1, column=0, sticky='n')
Hour.set(HourSetEntry)

#Setting up the seconds for the alarm
MinutesSet = tk.Label(mainWindow, text='MINUTES').grid(row=2, column=0, sticky='nw', padx=10)
MinuteSetEntry= tk.Entry(mainWindow, width=25, textvariable=minutes).grid(row=2, column=0, sticky='n')
minutes.set(MinuteSetEntry)
# Set up the am pm box for the alarm
# am = tk.Checkbutton(mainWindow, text='am', textvariable=a).grid(row=3, column=0, sticky='w')
# pm = tk.Checkbutton(mainWindow, text='PM', textvariable=p).grid(row=3, column=0, sticky='e')
# set up the button for the alarm set
SetAlarm = tk.Button(mainWindow, text="Set Alarm", command=Alarm).grid(row=4, column=0)
time()
mainWindow.mainloop()