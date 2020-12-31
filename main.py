import pyttsx3 #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os

print("Initializing Chip")
MASTER = "Sonu"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#speak function will speak the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This function will wish you as per the current time in your clock
def wishMe():
    hour= int(datetime.datetime.now().hour) 

    if hour>=0 and hour<12:
        speak("Good Morning"+ MASTER)
    elif(hour>=12 and hour<18):
        speak("Good Afternoon"+ MASTER)
    else:
        speak("Good Evening"+ MASTER)

#This command will take a microphone input
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
         print("say that again please")
         query = None
    return query

#Main program starts here

def main():
    speak("Initializing Chip...")
    wishMe()
    query = takeCommand()

    #Logic for executing basic tasks as per the query

    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)
    elif 'open youtube' in query.lower():
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        url = "google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open amazon' in query.lower():
        url = "amazon.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir="C:\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[2]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"{MASTER} the time is {strTime}")
        
    elif 'open code' in query.lower():
        codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

main()
