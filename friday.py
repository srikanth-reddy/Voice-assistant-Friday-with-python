#01 first
'''
import pyttsx3 #pip install pyttsx3

engine = pyttsx3.init()
engine.say("This is friday")
engine.runAndWait()
'''
#02 define function
'''
import pyttsx3 #pip install pyttsx3

engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("This is Friday")
'''
#03 voice and rate of speed
'''
import pyttsx3 #pip install pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hello! This is python assistant tutorial")
'''
#04 datetime
'''
import pyttsx3 #pip install pyttsx3
import datetime

engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

time()
'''
#05 datetime 2
'''
import pyttsx3 #pip install pyttsx3
import datetime

engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

date()
'''
#06 greet us function
'''
import pyttsx3 #pip install pyttsx3
import datetime

engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!")
    time()
    date()
    speak("Friday at your service. How can i help you?")

wishme()
'''
#07 wish me function
'''
import pyttsx3 #pip install pyttsx3
import datetime

engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening")
    elif hour >= 24 and hour <= 6:
        speak("Good Night")
    
    speak("Friday at your service. How can i help you?")

wishme()
'''
# Take command function
'''
import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
engine = pyttsx3.init() #pip install pipwin 
def speak(audio):#then pipwin install pyaudio
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening")
    elif hour >= 24 and hour <= 6:
        speak("Good Night")
    
    speak("Friday at your service. How can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
    
        return "None"

    return query

takeCommand()
'''
# main function
'''
import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
engine = pyttsx3.init() #pip install pipwin 
def speak(audio):#then pipwin install pyaudio
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening")
    elif hour >= 24 and hour <= 6:
        speak("Good Night")
    
    speak("Friday at your service. How can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
    
        return "None"

    return query

if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
'''
# Wikipedia
'''
import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
 #pip install pipwin
 #then pipwin install pyaudio
import wikipedia #pip install wikipedia
engine = pyttsx3.init() 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening")
    elif hour >= 24 and hour <= 6:
        speak("Good Night")
    
    speak("Friday at your service. How can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
    
        return "None"

    return query

if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
'''
#Send Email
'''
import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
 #pip install pipwin
 #then pipwin install pyaudio
import wikipedia #pip install wikipedia
import smtplib
engine = pyttsx3.init() 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening")
    elif hour >= 24 and hour <= 6:
        speak("Good Night")
    
    speak("Friday at your service. How can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
    
        return "None"

    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('test@gmail.com',"password")
    server.sendmail("test@gmail.com", to, content)
    server.close()


if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendmail(to, content)
                #comment above line
                #speak(content) this is to read the content
                speak("Email Sent suucessfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
'''
#Chrome Search
'''
import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
 #pip install pipwin
 #then pipwin install pyaudio
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb

engine = pyttsx3.init() 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening")
    elif hour >= 24 and hour <= 6:
        speak("Good Night")
    
    speak("Friday at your service. How can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
    
        return "None"

    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('test@gmail.com',"password")
    server.sendmail("test@gmail.com", to, content)
    server.close()


if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendmail(to, content)
                #comment above line
                #speak(content) this is to read the content
                speak("Email Sent suucessfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        elif "search in chrome" in query:
            speak("what should I search?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")
'''
#Logout,Restart & Shutdown function
'''
import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
 #pip install pipwin
 #then pipwin install pyaudio
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os

engine = pyttsx3.init() 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening")
    elif hour >= 24 and hour <= 6:
        speak("Good Night")
    
    speak("Friday at your service. How can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
    
        return "None"

    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('test@gmail.com',"password")
    server.sendmail("test@gmail.com", to, content)
    server.close()


if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendmail(to, content)
                #comment above line
                #speak(content) this is to read the content
                speak("Email Sent suucessfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        elif "search in chrome" in query:
            speak("what should I search?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")
        elif "logout" in query:
            os.system("Shutdown - l")
        elif "shutdown" in query:
            os.system("Shutdown /s /t l")
        elif "restart" in query:
            os.system("Shutdown /r /t l")
'''
#play songs
import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
 #pip install pipwin
 #then pipwin install pyaudio
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes

engine = pyttsx3.init() 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening")
    elif hour >= 24 and hour <= 6:
        speak("Good Night")
    
    speak("Friday at your service. How can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
    
        return "None"

    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('test@gmail.com',"password")
    server.sendmail("test@gmail.com", to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:/Udemy python/ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = psutil.sensors_battery()#it is list so we can't type cast it into string
    speak("battery is at")
    speak(battery.percent )

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendmail(to, content)
                #comment above line
                #speak(content) this is to read the content
                speak("Email Sent suucessfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        elif "search in chrome" in query:
            speak("what should I search?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")
        elif "log out" in query:
            os.system("Shutdown - l")
        elif "shutdown" in query:
            os.system("Shutdown /s /t l")
        elif "restart" in query:
            os.system("Shutdown /r /t l")

        elif "play songs" in query:
            songs_dir = "D:\Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "remember that" in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("you said me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("you said to remember that" + remember.read())
        # screenshot function
        elif "screenshot" in query:
            screenshot()
            speak("done!")
        #cpu and battery percentage
        elif "cpu" in query:
            cpu()
        #joke function
        elif "joke" in query:
            jokes()