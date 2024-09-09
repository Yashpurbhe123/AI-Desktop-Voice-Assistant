import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from ecapture import ecapture as ec
import pyjokes
import time
import pywhatkit
from PIL import Image   
from urllib.request import urlopen
import json
import pyautogui
class VoiceAssistant:
    
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def wishMe(self):

        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            self.speak("Good Morning,Sir!")
        elif 12 <= hour < 18:
            self.speak("Good Afternoon,Sir!")
        else:
            self.speak("Good Evening,Sir!")

        self.speak("How can I help you?")

    def takequery(self):

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
            print("Say that again, please...")
            return "None"
        return query

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.wishMe()
    
    while True:
        query = assistant.takequery().lower()

        if 'tell me about' in query or 'who is' in query:
            assistant.speak('Searching information,sir.')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            assistant.speak("According to Wikipedia")
            print(results)
            assistant.speak(results)

        elif "open wikipedia" in query or "wikipedia" in query:
            assistant.speak('ok sir')
            webbrowser.open_new_tab("https://www.wikipedia.org/")

        elif 'open youtube' in query or "youtube" in query:
            assistant.speak('ok sir , opening youtube')
            webbrowser.open_new_tab("youtube.com")

        elif 'open google' in query or "google" in query:
            assistant.speak('ok sir, opening google')
            webbrowser.open_new_tab("google.com")

        elif 'play music' in query or "music" in query:
            assistant.speak('yes sir , playing music')
            music_dir = " "                                 #add own music application path
            songs = os.listdir(music_dir)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'open stack overflow' in query:
            assistant.speak('ok sir')
            webbrowser.open_new_tab("stackoverflow.com")
        
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M")
            assistant.speak(f"Sir, the time is {strTime}")

        elif 'what is the date' in query:
            strTime = datetime.datetime.now().strftime("%d-%M-%Y")
            assistant.speak(f"Sir, the date is {strTime}")

        elif 'tell me the latest news' in query or "tell me the news"in query or "latest news" in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=in&apiKey=1cc4096fa7db40e4a7cac2638854e4d3")
                data = json.load(jsonObj)
                i = 1
                assistant.speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                    if i > 4:
                        break   
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    assistant.speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))

        if 'play' in query:
            song = query.replace('play', '')
            assistant.speak('playing' + song)
            pywhatkit.playonyt(song)

        if 'jarvis' in query:
            assistant.speak('yes sir')

        if 'how are you' in query or "hu r u" in query:
            assistant.speak('I am fine sir, thank you for asking')
            assistant.speak('how are you sir')

        if 'fine' in query or "good" in query:
            assistant.speak("It's good to know that your fine,how i can help you")

        if 'what are you doing' in query:
            assistant.speak('nothing sir')

        if 'what is your use' in query:
            assistant.speak('i am designed to, minimise human work by, automation')

        if "who are you" in query:
            assistant.speak("I am a virtual assistant. I am programmed to minor tasks, like, opening youtube, google, gmail and many more, predict time, take a photo, searching information on browser and wikipedia also, predict weather in different cities, get top headline news from times of india, and you can ask me computational or geographical questions too!")

        if "who made you" in query or "who created you" in query:
            assistant.speak("I have been created by, Yash, and his team.")

        if 'reason for you' in query:
            assistant.speak("I was created as a Minor project by Mr yash ")

        if "why you came to world" in query:
            assistant.speak("Thanks to YASH. further It's a secret")

        if "thank you" in query:
            assistant.speak("wost welcome sir !")

        if 'are you single' in query:
            assistant.speak("I am in a relationship with wifi")

        elif "joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            assistant.speak(joke)

        elif 'write a note' in query:
            assistant.speak("What should i write, sir")
            note = assistant.takequery()
            file = open('jarvis.txt', 'w')
            assistant.speak("Sir, Should i include date and time")
            snfm = assistant.takequery()
            assistant.speak("Ok sir")
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "tell me the note" in query or "tell the note" in query:
            assistant.speak("yes sir, telling Notes")
            file = open("jarvis.txt", "r")
            assistant.speak(file.read())


        elif 'open code' in query or "code" in query:
            assistant.speak('ok sir , opening vs code')
            codePath = ""                                   #Add your own Vs code path
            os.startfile(codePath)

        elif 'open powerpoint' in query or "powerpoint" in query:
                assistant.speak('ok sir')
                codePath = ""                                #Add your Own powerpoint path
                os.startfile(codePath)

        elif 'open excel' in query:
            assistant.speak('Ok sir')
            codePath = ""                                      #Add your Own Excel path
            os.startfile(codePath)

        elif 'open paint' in query:
            assistant.speak('Ok sir , Opening paint')
            codePath = ""                                       #Add your Own Paint path              
            os.startfile(codePath)

        elif 'open word' in query:
            assistant.speak('ok sir, Opening word')
            codePath = ""                                        #Add your Own Word path
            os.startfile(codePath)

        elif 'open spotify' in query:
            assistant.speak('ok sir')
            codePath = ""                                       #Add your Own Spotify path
            os.startfile(codePath)

        elif 'open telegram' in query:
            assistant.speak('ok sir')
            codePath = ""                                       #Add your Own Telegram path
            os.startfile(codePath)

        elif 'take a photo' in query or "take a selfie" in query:
            assistant.speak('ok sir , taking photo')
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            assistant.speak("It is located in ")
            assistant.speak(location)
            webbrowser.open_new_tab("https://www.google.com/maps/place/" + location + "")

        elif 'search about' in query or 'how to make' in query or "who is" in query:
            assistant.speak('here it is the result sir')
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)

        elif "switch the window" in query or "switch window" in query:
            assistant.speak("Okay sir, Switching the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(5)
            pyautogui.keyUp("alt")
    
        elif 'stop' in query:
            assistant.speak('OK,sir')
            break
