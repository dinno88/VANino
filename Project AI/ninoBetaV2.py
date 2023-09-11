import speech_recognition as sr
import openai
import wikipedia
import webbrowser
import os
import datetime
import pyttsx3
from googletrans import Translator

print("Your Assistant is here..")

MASTER = "Dinno"

#set up the text to speech engine
engine = pyttsx3.init()
#set up the translator
translator = Translator()
#set up the rate of the speech to a slower speech
engine.setProperty('rate', 180)
#set up the language of the speech
engine.setProperty('voices', 'en')
# activationWord = 'computer'

#set up the OpenAI API Client
openai.api_key = "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"
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

    if query == "Who are you" in query.lower():
        query = ""
        msquery = ""
        speak("I am Nino.. Your Assistance")
    elif "wikipedia" in query.lower():
        speak("searching on Wikipedia...")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        print(result)
        speak(result)
    elif "open google" in query.lower():
        url = "google.com" 
        msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
        speak("Ok Opening Google on Microsoft Edge")
        webbrowser.get(msedge_path).open(url)
    elif "open youtube" in query.lower():
        url = "youtube.com" 
        msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
        speak("Ok Opening Youtube on Microsoft Edge")
        webbrowser.get(msedge_path).open(url)
    elif "open facebook" in query.lower():
        url = "facebook.com" 
        msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
        speak("Ok Opening Facebook on Microsoft Edge")
        webbrowser.get(msedge_path).open(url)
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
    elif 'thanks' in query.lower():
        speak(f"My Pleasure {MASTER}, Glad to help you!")
        response = ""
        exit()
    else:
        response = generate_response(prompt=query)
        # print(f"Here some Information for you, {MASTER}")
        print(f"Assistant: {response}")

        engine.say("")
        engine.say(response)
        engine.runAndWait()

except sr.UnknownValueError:
    print(f"Sorry, {MASTER} something went wrong...")
except sr.RequestError as e:
    print(f"Sorry, {MASTER} error while processing voice command : {e}")

# while True:
#     query = generate_response('prompt').lower().split()
#     if query[0] == activationWord:
#         query.pop(0)
#         if query[0] == 'say':
#             if'hello' in query:
#                 speak(f"Hai,{MASTER}")
#             else: 
#                 query.pop(0)
#                 speech = ''.join(query)
    
