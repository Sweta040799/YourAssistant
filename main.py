import speech_recognition as sr
import pyttsx3
import pywhatkit

hear = sr.Recognizer()
engine = pyttsx3.init()

def intro():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("Hello I'm your assistant, which song will you like to listen")
    engine.runAndWait()
    return hear

def callAssistant():
    try :
       with sr.Microphone() as origin:
           print("Listening....")
           sound = hear.listen(origin)

           text = hear.recognize_google(sound)
           text = text.lower()
           text = text.replace("assistant", '')
           if 'play' in text:
              print('Please Wait, Playing....')
              engine.say("Please Wait, Playing...")
              engine.runAndWait()
              text = text.replace("play", '')
              pywhatkit.playonyt(text)
              engine.runAndWait()


    except :
        print("Microphone is not working or check your internet connection")
        engine.say("Microphone is not working or check your internet connection")
        engine.runAndWait()

intro()
callAssistant()