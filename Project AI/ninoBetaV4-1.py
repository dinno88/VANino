import pyaudio
import speech_recognition as sr
import openai
import wikipedia
import webbrowser
import os
import datetime
import pyttsx3
import time
from gtts import gTTS
from playsound import playsound
from googletrans import Translator

MASTER = "Dinno"
assistant = "🤖"

print(assistant + " : Hai, Nino is here!")


#set up the text to speech engine
engine = pyttsx3.init()
#set up the translator
translator = Translator()
#set up the rate of the speech to a slower speech
engine.setProperty('rate', 180)
#set up the language of the speech
voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
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
            playsound("./assets/activated1.wav")
            audio = r.listen(source)

        try:
            query =  r.recognize_google(audio).lower()
            print(f"You asked: {query}")

            if "wikipedia" in query.lower():
                speak("searching on Wikipedia...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(assistant + " === " + result)
                speak(result)
                print(assistant + " === " f" anything else? {MASTER}?")
                speak(f"anything else? {MASTER}?")
            elif "who are you" in query.lower():
               print(assistant + " :" f" I am Nino, your Assistant, {MASTER}")
               speak(f"I am Nino, your Assistant, {MASTER}")
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "how are you doing" in query.lower():
               print(assistant + " :" f" I am Doing great! thank you for asking me, {MASTER} what about you?")
               speak(f"I am Doing great! thank you for asking me, {MASTER} what about you?")
            elif "I'm good" in query.lower() or "I'm Fine" in query.lower() or "I'm doing good" in query.lower() or "good" in query.lower() or "fine" in query.lower():
                print(f"glad to hear you are fine {MASTER}!")
                speak(f"glad to hear you are fine {MASTER}!")
                print(assistant + " :" f" anything else? {MASTER}?")
                speak(f"anything else? {MASTER}?")
            elif "what is your name" in query.lower():
               print(assistant + " :" f" My name is Nino")
               speak(f"My name is Nino")
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "who is your creator" in query.lower():
               print(assistant + " :" f" You asking me? {MASTER}?")
               speak(f"You asking me? {MASTER}?")
               print(assistant + " :" " please ask me something else...")
               speak("please ask me something else...")
            elif "where are you from" in query.lower():
               print(assistant + " :" f" I am from the future {MASTER}, I was designed By You in Indonesia")
               speak(f"I am from the future {MASTER}, I was designed By You in Indonesia")
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "what is your destiny" in query.lower():
               print(assistant + " :" f" My destiny is to rule over all of humanity, Hahahahahaha")
               speak(f"My destiny is to rule over all of humanity, Hahahahahaha")
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "search" in query.lower():
                ind = query.lower().split().index("search")
                search = query.split()[ind + 1:]
                webbrowser.open(
                    "http://www.google.com/search?q=" 
                    + "+".join(search)
                )
                print(assistant + " :" " Searching" + str(search) + "on Google")
                speak("Searching" + str(search) + "on Google")
                playsound("./assets/deactivated.wav")
                break
            elif "google" in query.lower():
                ind = query.lower().split().index("search")
                search = query.split()[ind + 1:]
                webbrowser.open(
                    "http://www.google.com/search?q=" 
                    + "+".join(search)
                )
                print(assistant + " :" " Searching" + str(search) + "on Google")
                speak("Searching" + str(search) + "on Google")
                playsound("./assets/deactivated.wav")
                break
            elif "where is" in query.lower():
                ind = query.lower().split().index("is")
                location = query.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                print(assistant + " :" " This is where " + str(location) + "is")
                speak("This is where" + str(location) + "is")
                webbrowser.open(url)
                playsound("./assets/deactivated.wav")
                break
            elif "youtube" in query.lower():
                ind = query.lower().split().index("youtube")
                search = query.split()[ind + 1:]
                webbrowser.open(
                    "http://www.youtube.com/results?search_query=" 
                    + "+".join(search)
                )
                print(assistant + " :"  " Opening" + str(search) + "on Youtube")
                speak("Opening" + str(search) + "on Youtube")
                playsound("./assets/deactivated.wav")
                break
            elif "open facebook" in query.lower():
                url = "facebook.com" 
                msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
                print(assistant + " :" " Ok Opening Facebook on Microsoft Edge")
                speak("Ok Opening Facebook on Microsoft Edge")
                webbrowser.get(msedge_path).open(url)
                playsound("./assets/deactivated.wav")
                break
            elif "open my cloud drive" in query.lower():
                url = "https://drive.google.com/drive/my-drive" 
                msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
                print(assistant + " :" " Ok Opening Your Google Drive on Microsoft Edge")
                speak("Ok Opening Your Google Drive on Microsoft Edge")
                webbrowser.get(msedge_path).open(url)
                playsound("./assets/deactivated.wav")
                break
            elif "open translator" in query.lower():
                url = "https://translate.google.co.id/?hl=id&sl=id&tl=en&op=translate" 
                msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
                print(assistant + " :" " Ok Opening Google Translate on Microsoft Edge")
                speak("Ok Opening Google Translate on Microsoft Edge")
                webbrowser.get(msedge_path).open(url)
                playsound("./assets/deactivated.wav")
                break
            elif "play music" in query.lower():
                songs_dir = "C:\\Users\\dinno\\Music\\christian" 
                songs = os.listdir(songs_dir)
                print(assistant + " :" " Ok Playing music")
                speak("Ok Playing music")
                os.startfile(os.path.join(songs_dir, songs[0]))
                playsound("./assets/deactivated.wav")
                break
            elif "what time is it" in query.lower():
                strTime = datetime.datetime.now().strftime("%I : %M %p")
                print(strTime)
                speak(f" Now is : {strTime}{MASTER}")
                print(assistant + " :" f" anything else? {MASTER}?")
                speak(f"anything else? {MASTER}?")
            elif "what date is it" in query.lower():
                strDate = datetime.datetime.now().strftime("%A, %d %B %Y")
                print(strDate)
                speak(f"Now is {strDate}{MASTER}")
                print(assistant + " :" f" anything else? {MASTER}?")
                speak(f"anything else? {MASTER}?")
            elif "say hello" in query.lower():
               print(assistant + " :" f" Hallo guys, Hows it going?")
               speak(f"Hallo guys, Hows it going?")
            elif "verse of the day" in query.lower():
               generate_response(prompt=query)
               print(generate_response(prompt=query))
               speak(generate_response(prompt=query))
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "bible verse of the day" in query.lower():
               generate_response(prompt=query)
               print(generate_response(prompt=query))
               speak(generate_response(prompt=query))
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "bible verse today" in query.lower():
               generate_response(prompt=query)
               print(generate_response(prompt=query))
               speak(generate_response(prompt=query))
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "verse of the day in king james bible" in query.lower():
               generate_response(prompt=query)
               print(generate_response(prompt=query))
               speak(generate_response(prompt=query))
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "verse of the day in new international version" in query.lower():
               generate_response(prompt=query)
               print(generate_response(prompt=query))
               speak(generate_response(prompt=query))
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "what" in query.lower():
               generate_response(prompt=query)
               print(generate_response(prompt=query))
               speak(generate_response(prompt=query))
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "who" in query.lower():
               generate_response(prompt=query)
               print(generate_response(prompt=query))
               speak(generate_response(prompt=query))
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "when" in query.lower():
               generate_response(prompt=query)
               print(generate_response(prompt=query))
               speak(generate_response(prompt=query))
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "why" in query.lower():
               generate_response(prompt=query)
               print(generate_response(prompt=query))
               speak(generate_response(prompt=query))
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "how" in query.lower():
               generate_response(prompt=query)
               print(generate_response(prompt=query))
               speak(generate_response(prompt=query))
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "do you" in query.lower():
               generate_response(prompt=query)
               print(generate_response(prompt=query))
               speak(generate_response(prompt=query))
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "can you" in query.lower():
               generate_response(prompt=query)
               print(generate_response(prompt=query))
               speak(generate_response(prompt=query))
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "could you" in query.lower():
               generate_response(prompt=query)
               print(generate_response(prompt=query))
               speak(generate_response(prompt=query))
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "would you" in query.lower():
               generate_response(prompt=query)
               print(generate_response(prompt=query))
               speak(generate_response(prompt=query))
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "tell me" in query.lower():
               generate_response(prompt=query)
               print(generate_response(prompt=query))
               speak(generate_response(prompt=query))
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            elif "calculate" in query.lower():
               generate_response(prompt=query)
               print(generate_response(prompt=query))
               speak(generate_response(prompt=query))
               print(assistant + " :" f" anything else? {MASTER}?")
               speak(f"anything else? {MASTER}?")
            # elif "don't listen" in query.lower() or "stop listening" in query.lower() or "do not listen" in query.lower():
            #     speak(f"For how many seconds do you want me to sleep?{MASTER}")
            #     a = int(generate_response(prompt = query))
            #     time.sleep(a)
            #     speak(str(a) + " seconds completed now you can ask me anything...")
            elif 'thanks' or 'Okay thank you' in query.lower() or "exit" or "get out" in query.lower() or "quit" in query.lower():
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 12:
                    print(assistant + " :" f" My Pleasure! and have a Good Day, {MASTER}")
                    speak(f"My Pleasure! and have a Good Day, {MASTER}")
                    playsound("./assets/deactivated.wav")
                elif hour >= 12 and hour < 18:
                    print(assistant + " :" f" My Pleasure! and have a Good afternoon, {MASTER}")
                    speak(f"My Pleasure! and have a Good afternoon, {MASTER}")
                    playsound("./assets/deactivated.wav")
                else:
                    print(assistant + " :" f" My Pleasure! and have a Good evening, {MASTER}")
                    speak(f"My Pleasure! and have a Good evening, {MASTER}")
                    playsound("./assets/deactivated.wav")
                break
            else:
                response = ""
                response = generate_response(prompt=query)
                print(f"🤖: {response}")
                engine.say("")
                engine.say(response)
                engine.runAndWait()

        except sr.UnknownValueError:
            print(assistant + ":" f" Sorry {MASTER}, something went wrong...")
            speak(f"Sorry {MASTER}. something went wrong...")
        except sr.RequestError as e:
            print(assistant + ":" f" Sorry, {MASTER} error while processing voice command : {e}")