import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
import pyautogui
import wikipedia
import pywhatkit as pwk 
import openai_request as ai

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices: 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command ():
    content =" "
    while content == " ":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listenning....")
            audio = r.listen(source)

        #recognize speech using Google Speech Recognition
        try:
            content = r.recognize_google(audio, language="en-in")
            print("Recognizing..." + content)
        except Exception as e:
            print("please try again....")

    return content 

def main_process():
    zara_chat = []
    while True:
        request = command().lower()
        if "hello" in request:
            print("welcome, how can i help you?")
            speak("welcome, how can i help you?")
            
        elif "play music" in request:
            speak("playing music...")
            song = random.randint(1,3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=XTp5jaRU3Ws")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=YsB4Vhlv8ns")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=Gz38Yj09k3A") 
        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("current time is " + str(now_time))
        elif "say date" in request:
            now_time = datetime.datetime.now().strftime("%d:%m:%Y")  # Day/Month/Year format
            speak("The current date is " + str(now_time))
        elif "open youtube" in request:
            webbrowser.open("www.youtube.com")
        elif "open" in request:
            query = request.replace("open ", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
        elif "wikipedia" in request:
            request = request.replace("Zara ", "")
            request = request.replace("search on wikipedia ", "")
            result = wikipedia.summary(request, sentences=2)
            speak(result)
        elif "search google" in request:
            request = request.replace("Zara ", "")
            request = request.replace("search google ", "")
            webbrowser.open("https://www.google.com/search?q="+request)
        elif "send whatsapp" in request:
            pwk.sendwhatmsg("+919650636381", "Hi, this message is from ZARA an AI chatbot created by Mr.shubham", 19, 58, 30)
        elif "ask ai " in request:
            zara_chat = []
            request = request.replace("Zara ", "")
            request = request.replace("Ask ai ", "")
            zara_chat.append({"role": "user","content": request})
 
            response = ai.send_request(zara_chat)
            print(request)
            speak(response)
        elif "clear chat" in request:
            zara_chat = []
            speak("chat cleared")
    
        else:
            request = request.replace("Zara", "")

            zara_chat.append({"role": "user","content": request})
            response = ai.send_request(zara_chat)

            zara_chat.append({"role": "assistant","content": response})
            print(response)
            speak(response)

main_process()

