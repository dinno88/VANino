import speech_recognition as sr
import openai
import wikipedia
import webbrowser
import os
import datetime
import pyttsx3
import wolframalpha
from googletrans import Translator

MASTER = "Dinno"
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# msedge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
# webbrowser.register('msedge', None, webbrowser.BackgroundBrowser(msedge_path))

def speak(text, rate = 150):
    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()
speak("Hai")

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
    pendengar = sr.Recognizer()
    print("I am Listening...")

    with sr.Microphone() as source:
        pendengar.pause_threshold = 2
        input_speech = pendengar.listen(source)
    try:
        print("Processing...")
        query = pendengar.recognize_google(input_speech, language='en_us')
        print(f"{MASTER} Your Command was : {query}")
    except Exception as exception:
        print("I did not quiet catch that")
        speak("I did not quiet catch that")
        print(exception)
        return 'None'
    return query

if __name__ == '__main__':
    while True:
        query = perintah()
        if "wikipedia" in query.lower():
            speak("searching on Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif "open translator" in query.lower():
            url = "https://translate.google.co.id/?hl=id&sl=id&tl=en&op=translate" 
            msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
            speak("Ok Opening Google Translate on Microsoft Edge")
            webbrowser.get(msedge_path).open(url)
        elif "play music" in query.lower():
            songs_dir = "C:\\Users\\dinno\\Music\\mp3" 
            songs = os.listdir(songs_dir)
            speak("Ok Playing Music")
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif "what time is it" in query.lower():
            strTime = datetime.datetime.now().strftime("%I : %M %p")
            print(strTime)
            speak(f"Now is {strTime}{MASTER}")
        elif "what date is it" in query.lower():
            strDate = datetime.datetime.now().strftime("%A, %d %B %Y")
            print(strDate)
            speak(f"Now is {strDate}{MASTER}")
        elif "who are you" in query.lower():
            print(f"I am Nino, your Assistant, {MASTER}")
            speak(f"I am Nino, your Assistant, {MASTER}")
        elif "where are you from" in query.lower():
            print(f"I am from the future, {MASTER}")
            speak(f"I am from the future, {MASTER}")
        elif "what is your destiny" in query.lower():
            print(f"My destiny is to rule over all of humanity, Hahahahahaha")
            speak(f"My destiny is to rule over all of humanity, Hahahahahaha")
        elif "thanks" or "Okay Nino thanks" in query.lower():
            speak(f"My Pleasure {MASTER}, Glad to help you!")
            exit()
            #     if query[0] == "say":
            #         if "hello" in query:
            #             print(f"Hello {MASTER}")
            #             speak(f"Hello {MASTER}")
            #         else: 
            #             query.pop(0)
            #             speech = ''.join(query)
            #             speak(speech)

            #     if query[0] == "go" and query[1] == "to":
            #             print(f"Opening... ")
            #             speak(f"Opening... ")
            #             query = ''.join(query[2:])
            #             webbrowser.get('msedge').open_new(query)
                
            #     if query[0] == "log":
            #         speak(f"What is your Note {MASTER}?")
            #         newNote = perintah().lower()
            #         now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            #         with open("note_%s.txt" % now, "w") as newFile:
            #             newFile.write(newNote)
            #         speak(f"{MASTER}, Note has Written")

            # if query[0] == "thanks" :
            #     print(f"Okay {MASTER}, my pleasure! ")
            #     speak(f"Okay {MASTER}, my pleasure! ")
            #     exit()

            # if query[0] == "who" and query[1] == "are":
            #     if "you" in query:
            #         query = ''.join(query[3:])
            #         print(f"I am Bumblebee, your Assistant, {MASTER}")
            #         speak(f"I am Bumblebee, your Assistant, {MASTER}")
            #     else: 
            #         query.pop(0)
            #         speech = ''.join(query)
            #         speak(speech)
            