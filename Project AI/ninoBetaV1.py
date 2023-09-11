# NinoProject
import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import re
import webbrowser
import os
import smtplib

print("Nino Is Here...")

MASTER = "Dinno"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
speak("Hai, Nino is here")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning{MASTER} How Can I Help you?")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon{MASTER} How Can I Help you?")
    else:
        speak(f"Good Evening{MASTER} How Can I Help you?")
        speak("")
wishMe()

def perintah():
    mendengar = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = mendengar.listen(source)
        try: 
            print('Please Wait...')
            speak('Please Wait...')
            dengar = mendengar.recognize_google(audio, language='en-us')
            print(f"Your Command:" + dengar + "\n")
        except sr.UnknownValueError:
            print(f"Sorry {MASTER} something went wrong..")
            speak(f"Sorry {MASTER} something went wrong..")
            dengar = perintah()
        return dengar

dengar = perintah()
if "wikipedia" in dengar.lower():
    speak("searching on Wikipedia...")
    dengar = dengar.replace("wikipedia", "")
    result = wikipedia.summary(dengar, sentences=2)
    print(result)
    speak(result)
elif "open google" in dengar.lower():
    url = "google.com" 
    msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
    speak("Ok Opening Google on Microsoft Edge")
    webbrowser.get(msedge_path).open(url)
    speak("Done!")
elif "open youtube" in dengar.lower():
    url = "youtube.com" 
    msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
    speak("Ok Opening Youtube on Microsoft Edge")
    webbrowser.get(msedge_path).open(url)
elif "open facebook" in dengar.lower():
    url = "facebook.com" 
    msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
    speak("Ok Opening Facebook on Microsoft Edge")
    webbrowser.get(msedge_path).open(url)
elif "open translator" in dengar.lower():
    url = "https://translate.google.co.id/?hl=id&sl=id&tl=en&op=translate" 
    msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
    speak("Ok Opening Google Translate on Microsoft Edge")
    webbrowser.get(msedge_path).open(url)
elif "play music" in dengar.lower():
    songs_dir = "C:\\Users\\dinno\\Music\\mp3" 
    songs = os.listdir(songs_dir)
    speak("Ok Playing Music")
    os.startfile(os.path.join(songs_dir, songs[0]))
elif "what time is it" in dengar.lower():
    strTime = datetime.datetime.now().strftime("%I : %M %p")
    print(strTime)
    speak(f"Now is {strTime}{MASTER}")
elif 'thanks' in dengar.lower():
    speak(f"My Pleasure {MASTER}, Glad to help you!")
    exit()


# while True:
#     perintah()