#greeting
first = input('Enter your first name:')
last = input('Enter your last name:')
text = ("Hello, Carl Clack!")

city = input('Enter the town or city where you live:')
text = (" You live in Spring Valley!")
answer = input("Correct or no?:")
age = input('Enter your age:')
text = ("You are 15 years old!")
answer = input("Correct or No?:")

#Baymax introduces himself
text = (" My name is Baymax!")
#calculator
num1 = input("Enter a number:")
num2 = input("Enter another number:")
result = float(num1) + float(num2)
print(result)

from datetime import date
today = date.today()
print("Current date:", today)

from gtts import gTTS 
import os

text = ("My name is Baymax!")

language = ('en')

speech = gTTS(text,'en', 'slow')

language = ('en')

speech.save("voice.mp3")

import pyttsx3
import webbrowser
import smtplib
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your digital assistant BAYMAX!')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        
if __name__ == '__main__':

  while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif ('bye') in query:
          speak('ok sir')
          speak('closing all systems')
          speak('disconnecting to servers')
          speak('going offline')
          quit() 
        
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')

def gooffline():
    speak('ok sir')
    speak('closing all systems')
    speak('disconnecting to servers')
    speak('going offline')
    quit() 

def speak(text):
    engine.say(text)
    engine.runAndWait()
def online():
    speak('starting all system applications')
    speak('installing all drivers')
    os.system('start E:/Rainmeter.exe')
    speak('every driver is installed')
    speak('all systems have been started')
    speak('now i am online sir')
    print('user')

speak('Next Command! Sir!')
