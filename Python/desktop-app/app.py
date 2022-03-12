from tkinter import *
import tkinter as tk
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
import pyautogui
import pyjokes
import pyperclip

##################
## Basic Config ##
##################

# Application Name
app_name = 'Voice Assistant'

# name of voice app
name = 'John'

# get system's current user
def get_current_user():
    return os.getlogin()

user = get_current_user() 

# get current working directory
working_directory = os.getcwd() 
 
# Window Configuration
window = tk.Tk()
width = 400
height = 600

# add image in photo variable and change its size
photo = PhotoImage(file = working_directory + '\\Python\\desktop-app\\assets\\mic.png')
photo = photo.subsample(3, 3)
img_label = Label(image=photo) 



###############
## Functions ##
###############


def test_command():
    speak("Testing")

def take_input():
    query = takeCommand().lower()
    # logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
        music_dir = 'D:\\Music'
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\" + get_current_user() + "\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    
    elif 'open code in current directory' in query:               
        codePath = "C:\\Users\\" + user + "\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        os.system("code . ") 
        
    elif 'joke' in query:
        speak(pyjokes.get_joke())
            
    elif 'screenshot' in query:
        screenshot = pyautogui.screenshot()
        screenshot.save(f"{user}-screenshot.png")
        speak("Done!")
        
    elif 'copy' in query:
        pyperclip.copy()
        speak("Done!")
            
    elif 'paste' in query:
        pyperclip.paste()
        speak("Done!")
            
    elif 'hi' in query:
        speak("Hello!")
            
    elif 'bye' in query:
        speak("Goodbye!")
                
                
    elif 'quit' in query:
        speak("Goodbye!")
        sys.exit()
 

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am "+ name +". Please tell me how may I help you")

     
def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email', 'your password')
    server.sendmail('your email', to, content)
    server.close()



#################
## Application ##
#################


class Application(Frame):
    # a button that has a mic icon on it
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.createWidgets()
         
    def createWidgets(self):
        # button = Button(window, image=photo,  borderwidth=0, command=test_command)
        button = Button(window, image=photo,  borderwidth=0, command=take_input)
        # center app
        button.place(relx=0.5, rely=0.5, anchor=CENTER)
       
          
window.title(app_name)
window.geometry(f"{width}x{height}")

app = Application(master=window)
app.mainloop()
