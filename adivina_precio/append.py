import pyttsx3
import speech_recognition as sr 


engine = pyttsx3.init()
ear = sr.Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("escuchando.....")
        audio = ear.listen(source)
        try:
            text = ear.recognize_google(audio, language = "es-ES")
            print(text)
            return text
        except sr.UnknownValueError:
            print("Failed to recognize")
            return 
        

if __name__ == "__main__":
    speak("prueba")
    listen()