import tkinter as tk
from tkinter import *
import datetime
import time
from threading import *
from turtle import width
import pyttsx3
import requests
from bs4 import BeautifulSoup


engine = pyttsx3.init()
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
# Weather function
def Weather():
    headers = {'User-Agent': 'user-agent'}
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
# Creating the Alarm MainScreen 
main_window = Tk()
main_window.title('My Python Alarm Clock')
# Set geometry
main_window.geometry("300x150")
def Time():
    todayTime = datetime.datetime.now().strftime('%I:%M:%S %p')
    timeLabel.config(text=todayTime)
    timeLabel.after(1000, Time)
timeLabel = tk.Label(main_window, font=('Roboto', 37, 'bold'), background ='#66ff00', foreground='#1900ff')
timeLabel.pack(pady=5)
Time()
# Use Threading
def Threading():
    hrs.config(bg='#5a5a5a', font=('calibri 10 bold'), foreground='#94ff4d')
    mins.config(bg='#5a5a5a', font=('calibri 10 bold'), foreground='#94ff4d')
    secs.config(bg='#5a5a5a', font=('calibri 10 bold'), foreground='#94ff4d')
    AM_PM.config(bg='#5a5a5a', font=('calibri 10 bold'), foreground='#94ff4d')
    t1=Thread(target=alarm)
    t1.start()
def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()} {am_pm.get()}" 
        time.sleep(1)
        # Getting the alarm and current time to set off the alarm 
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print(current_time,set_alarm_time)
        if current_time == set_alarm_time:
            speak(f'Good Morning The Current time is {current_time}')
            speak('The Weather Today is Looking')
            Weather()
            speak('In World News Today')
            WorldNews()     
# Add Labels, Frame, Button, Option menus
frame = Frame(main_window)
frame.pack()
# setting up the hours
hour = StringVar(main_window)
hours = ('01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12')
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.config(bg='#94ff4d', font=('calibri 10 bold'), foreground='#1900ff')
hrs.pack(side=LEFT)
# setting up the minutes 
minute = StringVar(main_window)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.config(bg='#94ff4d', font=('calibri 10 bold'), foreground='#1900ff')
mins.pack(side=LEFT)
# setting up the seconds 
second = StringVar(main_window)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
secs = OptionMenu(frame, second, *seconds)
secs.config(bg='#94ff4d', font=('calibri 10 bold'), foreground='#1900ff')
secs.pack(side=LEFT)
# setting up the AM or PM
am_pm = StringVar(main_window)
am_Pm = ('AM', 'PM')
am_pm.set(am_Pm[0])
AM_PM = OptionMenu(frame, am_pm, *am_Pm)
AM_PM.config(bg='#94ff4d', font=('calibri 10 bold'), foreground='#1900ff')
AM_PM.pack(side=LEFT)
Button(main_window,text="SET ALARM",font=("Roboto 15 bold"),command=Threading, background ='#94ff4d', foreground='#1900ff', width=300).pack(pady=5, padx=5) 
main_window.mainloop()
