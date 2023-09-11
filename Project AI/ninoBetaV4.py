import speech_recognition as sr
import openai
import wikipedia
import webbrowser
import os
import datetime
import pyttsx3
import sys
import requests
from googletrans import Translator
from bs4 import BeautifulSoup

MASTER = "Dinno"

print("==================")
print("Hai, Nino is here!")
print("==================")


#set up the text to speech engine
engine = pyttsx3.init()
#set up the translator
translator = Translator()
#set up the rate of the speech to a slower speech
engine.setProperty('rate', 150)
#set up the language of the speech
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
# activationWord = 'computer'

#set up the OpenAI API Client
openai.api_key = "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"

def speak(text):
    engine.say(text)
    engine.runAndWait()
speak(" ")

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

if __name__ == '__main__':
    while True:
        def generate_response(prompt):
            response = openai.Completion.create(
                engine = "text-davinci-002",
                prompt = prompt,
                max_tokens = 1024,
                n = 1,
                stop = None,
                temperature = 0.5,
            ) 
            return response.choices[0].text

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            query =  r.recognize_google(audio).lower()
            print(f"You asked: {query}")

            if "wikipedia" in query.lower():
                speak("searching on Wikipedia...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
                speak(f"anything else? {MASTER}?")
            elif "who are you" in query.lower():
               print(f"I am Nino, your Assistant, {MASTER}")
               speak(f"I am Nino, your Assistant, {MASTER}")
               speak(f"anything else? {MASTER}?")
            elif "where are you from" in query.lower():
               print(f"I am from the future, {MASTER}")
               speak(f"I am from the future, {MASTER}")
               speak(f"anything else? {MASTER}?")
            elif "what is your destiny" in query.lower():
               print(f"My destiny is to rule over all of humanity, Hahahahahaha")
               speak(f"My destiny is to rule over all of humanity, Hahahahahaha")
               speak(f"anything else? {MASTER}?")
            elif "open google" in query.lower():
                url = "google.com" 
                msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
                print("Ok Opening Google on Microsoft Edge")
                speak("Ok Opening Google on Microsoft Edge")
                webbrowser.get(msedge_path).open(url)
                break
            elif "open youtube" in query.lower():
                url = "youtube.com" 
                msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
                print("Ok Opening Youtube on Microsoft Edge")
                speak("Ok Opening Youtube on Microsoft Edge")
                webbrowser.get(msedge_path).open(url)
                break
            elif "open facebook" in query.lower():
                url = "facebook.com" 
                msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
                print("Ok Opening Facebook on Microsoft Edge")
                speak("Ok Opening Facebook on Microsoft Edge")
                webbrowser.get(msedge_path).open(url)
                break
            elif "open my drive google" in query.lower():
                url = "https://drive.google.com/drive/my-drive" 
                msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
                print("Ok Opening Your Google Drive on Microsoft Edge")
                speak("Ok Opening Your Google Drive on Microsoft Edge")
                webbrowser.get(msedge_path).open(url)
                break
            elif "open translator" in query.lower():
                url = "https://translate.google.co.id/?hl=id&sl=id&tl=en&op=translate" 
                msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
                print("Ok Opening Google Translate on Microsoft Edge")
                speak("Ok Opening Google Translate on Microsoft Edge")
                webbrowser.get(msedge_path).open(url)
                break
            elif "play music" in query.lower():
                songs_dir = "C:\\Users\\dinno\\Music\\mp3" 
                songs = os.listdir(songs_dir)
                print("Ok Playing Music")
                speak("Ok Playing Music")
                os.startfile(os.path.join(songs_dir, songs[0]))
                break
            elif "what time is it" in query.lower():
                strTime = datetime.datetime.now().strftime("%I : %M %p")
                print(strTime)
                speak(f"Now is {strTime}{MASTER}")
                speak(f"anything else? {MASTER}?")
            elif "what date is it" in query.lower():
                strDate = datetime.datetime.now().strftime("%A, %d %B %Y")
                print(strDate)
                speak(f"Now is {strDate}{MASTER}")
                speak(f"anything else? {MASTER}?")
            elif 'nothing' or 'thanks' or 'Okay thank you' in query.lower():
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 12:
                    print(f"My Pleasure! and have a Good Morning, {MASTER}")
                    speak(f"My Pleasure! and have a Good Morning, {MASTER}")
                elif hour >= 12 and hour < 18:
                    print(f"My Pleasure! and have a Good Afternoon, {MASTER}")
                    speak(f"My Pleasure! and have a Good Afternoon, {MASTER}")
                else:
                    print(f"My Pleasure! and have a Good Evening, {MASTER}")
                    speak(f"My Pleasure! and have a Good Evening, {MASTER}")
                response = ""
                exit()
            else:
                response = generate_response(prompt=query)
                print(f"Assistant: {response}")
                engine.say("")
                engine.say(response)
                engine.runAndWait()

        except sr.UnknownValueError:
            print(f"Sorry, {MASTER} something went wrong...")
            speak(f"Sorry, {MASTER} something went wrong...")
        except sr.RequestError as e:
            print(f"Sorry, {MASTER} error while processing voice command : {e}")
