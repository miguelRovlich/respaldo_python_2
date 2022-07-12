import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[1].id)
engine.say("Hola, ¿cómo te llamas?")
engine.runAndWait()
try:
    with sr.Microphone() as source:
        print("Escuchando!")
        voice = listener.listen(source)
        recognizer = listener.recognize_google(voice)
        print(recognizer)
except:
    pass