import pyjokes
import pywhatkit
import pyttsx4
import datetime
import os
import speech_recognition as sr
# import openai
import webbrowser
import wikipedia
from playsound import playsound
# from googletrans import Translator

MASTER = "Dinno"
assistant = "🤖"

print(assistant + " : Hai, Nino is here!")

#set up the text to speech engine
engine = pyttsx4.init()
#set up the translator
# translator = Translator()
#set up the rate of the speech to a slower speech
engine.setProperty('rate', 180)
#set up the language of the speech
voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
engine.setProperty("voice", voices[1].id)
# activationWord = 'computer'
#set up the OpenAI API Client
# openai.api_key = "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"

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
            # playsound("./assets/activated1.wav")
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
            elif "Hallo" in query.lower() or "Hello" in query.lower():
                print(assistant + " :" f" Hi {MASTER}! 😃")
                speak(f"Hi {MASTER}!")
                print(assistant + " :" f" How are you doing {MASTER}? 😃")
                speak(f"How are you doing {MASTER}?")
            elif "how is it going" in query.lower() or "how's it going" in query.lower() or "what's up" in query.lower() or "how are you" in query.lower() or "how are you doing" in query.lower():
                print(assistant + " :" f" I am Doing great! thank you for asking me, {MASTER} what about you?")
                speak(f"I am Doing great! thank you for asking me, {MASTER} what about you?")
            elif "who are you" in query.lower():
                print(assistant + " :" f" I am Nino, your Assistant, {MASTER}")
                speak(f"I am Nino, your Assistant, {MASTER}")
                print(assistant + " :" f" ask me something if you need help, {MASTER}!")
                speak(f"ask me something if you need help, {MASTER}!")
            elif "I'm good" in query.lower() or "I'm Fine" in query.lower() or "I'm doing good" in query.lower() or "good" in query.lower() or "fine" in query.lower():
                print(assistant + " :" f" glad to hear you are fine {MASTER}! 😍🥰😘")
                speak(f"glad to hear you are fine {MASTER}!")
                print(assistant + " :" f" anything else? {MASTER}?")
                speak(f"anything else? {MASTER}?")
            elif "what is your name" in query.lower():
                print(assistant + " : My name is Nino")
                speak("My name is Nino")
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
                print(assistant + " : My destiny is to rule over all of humanity, Hahahahahaha")
                speak("My destiny is to rule over all of humanity, Hahahahahaha")
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
                os.system("cls")
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
                os.system("cls")
                break
            elif "where is" in query.lower():
                ind = query.lower().split().index("is")
                location = query.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                print(assistant + " :" " This is where " + str(location) + "is")
                speak("This is where" + str(location) + "is")
                webbrowser.open(url)
                playsound("./assets/deactivated.wav")
                os.system("cls")
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
                os.system("cls")
                break
            elif "open facebook" in query.lower():
                url = "facebook.com" 
                msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
                print(assistant + " :" " Ok Opening Facebook on Microsoft Edge")
                speak("Ok Opening Facebook on Microsoft Edge")
                webbrowser.get(msedge_path).open(url)
                playsound("./assets/deactivated.wav")
                os.system("cls")
                break
            elif "open my cloud drive" in query.lower():
                url = "https://drive.google.com/drive/my-drive" 
                msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
                print(assistant + " :" " Ok Opening Your Google Drive on Microsoft Edge")
                speak("Ok Opening Your Google Drive on Microsoft Edge")
                webbrowser.get(msedge_path).open(url)
                playsound("./assets/deactivated.wav")
                os.system("cls")
                break
            elif "open translator" in query.lower():
                url = "https://translate.google.co.id/?hl=id&sl=id&tl=en&op=translate" 
                msedge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
                print(assistant + " :" " Ok Opening Google Translate on Microsoft Edge")
                speak("Ok Opening Google Translate on Microsoft Edge")
                webbrowser.get(msedge_path).open(url)
                playsound("./assets/deactivated.wav")
                os.system("cls")
                break
            elif "play music" in query.lower():
                songs_dir = "C:\\Users\\dinno\\Music\\christian" 
                songs = os.listdir(songs_dir)
                print(assistant + " :" " Ok Playing music")
                speak("Ok Playing music")
                os.startfile(os.path.join(songs_dir, songs[0]))
                playsound("./assets/deactivated.wav")
                os.system("cls")
                break
            elif "play" in query.lower():
                song = query.replace("play", '')
                print(assistant + " :"  " Opening" + song + "on Youtube")
                speak("Opening " + song + " on Youtube")
                pywhatkit.playonyt(song)
                os.system("cls")
                break
            elif "show me" in query.lower():
                something = query.replace("show me", '')
                print(assistant + " :"  " Opening" + something + "on Youtube")
                speak("Opening" + something + "on Youtube")
                pywhatkit.playonyt(something)
                os.system("cls")
                break
            elif "joke" in query.lower() or "jokes" in query.lower() or "another joke" in query.lower() or "another jokes" in query.lower():
                speak(pyjokes.get_joke())
                print(pyjokes.get_joke())
                print(assistant + " :" f" anything else? {MASTER}?")
                speak(f"anything else? {MASTER}?")
            elif "what time is it" in query.lower() or "what is the time" in query.lower():
                strTime = datetime.datetime.now().strftime("%I : %M %p")
                print(strTime)
                speak(f" Now is : {strTime}, {MASTER}")
                print(assistant + " :" f" anything else? {MASTER}?")
                speak(f"anything else? {MASTER}?")
            elif "what date is it" in query.lower():
                strDate = datetime.datetime.now().strftime("%A, %d %B %Y")
                print(strDate)
                speak(f"Now is {strDate}, {MASTER}")
                print(assistant + " :" f" anything else? {MASTER}?")
                speak(f"anything else? {MASTER}?")
            elif "say hello" in query.lower():
                print(assistant + " : Hallo guys, Hows it going? 😃")
                speak("Hallo guys, Hows it going?")
            elif "what" in query.lower() or "who" in query.lower() or "when" in query.lower() or "why" in query.lower() or "how" in query.lower():
                generate_response(prompt=query)
                print(generate_response(prompt=query))
                speak(generate_response(prompt=query))
                print(assistant + " :" f" anything else? {MASTER}?")
                speak(f"anything else? {MASTER}?")
            elif "do you" in query.lower() or "can you" in query.lower() or "could you" in query.lower() or "would you" in query.lower() or "tell me" in query.lower():
                generate_response(prompt=query)
                print(generate_response(prompt=query))
                speak(generate_response(prompt=query))
                print(assistant + " :" f" anything else? {MASTER}?")
                speak(f"anything else? {MASTER}?")
            elif "calculate" in query.lower() or "count" in query.lower() or "about" in query.lower():
                generate_response(prompt=query)
                print(generate_response(prompt=query))
                speak(generate_response(prompt=query))
                print(assistant + " :" f" anything else? {MASTER}?")
                speak(f"anything else? {MASTER}?")
            elif "thank's" in query.lower() or "thank you" in query.lower() or "no thank you" in query.lower() or "no thank's" in query.lower() or "Okay thank you" in query.lower() or "exit" in query.lower() or "get out" in query.lower() or "quit" in query.lower():
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 12:
                    print(assistant + " :" f" My Pleasure! and have a Good Day, {MASTER}")
                    speak(f"My Pleasure! and have a Good Day, {MASTER}")
                    playsound("./assets/deactivated.wav")
                    os.system("cls")
                elif hour >= 12 and hour < 18:
                    print(assistant + " :" f" My Pleasure! and have a Good afternoon, {MASTER}")
                    speak(f"My Pleasure! and have a Good afternoon, {MASTER}")
                    playsound("./assets/deactivated.wav")
                    os.system("cls")
                else:
                    print(assistant + " :" f" My Pleasure! and have a Good evening, {MASTER}")
                    speak(f"My Pleasure! and have a Good evening, {MASTER}")
                    playsound("./assets/deactivated.wav")
                    os.system("cls")
                break
            else:
                response = ""
                response = generate_response(prompt=query)
                print(f"🤖: {response}")
                engine.say("")
                engine.say(response)
                engine.runAndWait()

        except sr.UnknownValueError:
            print(assistant + ":" f" Sorry {MASTER}, I didn't quite catch that...")
            speak(f"Sorry {MASTER}. I didn't quite catch that...")
        except sr.RequestError as e:
            print(assistant + ":" f" Sorry, {MASTER} error while processing voice command : {e}")