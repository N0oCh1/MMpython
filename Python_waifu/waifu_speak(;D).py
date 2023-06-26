import pyttsx3 
import speech_recognition as sr
import re


def main():
    speak()
    name = lisent()
    answer(name)


def speak():
    engine = pyttsx3.init()
    engine.say("hola, muy buenas, como te llamas?")
    engine.runAndWait()


def lisent():
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("puedes hablar")
        audio = r.listen(sourse)
        text = r.recognize_google(audio, language = "es-ES")
        print(text)
        name = find_name(text)
        return name
    

def find_name(text):
    name = None
    patterns = ["llamo ([A-Za-záéíóúñÑ]+)", "mi nombre es ([A-Za-záéíóúñÑ]+)", "^([A-Za-záéíóúñÑ]+)$"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)[0]
        except IndexError:
            print("Could not find name")
            pass
    print(name)
    return name


def answer(name):
    engine = pyttsx3.init()
    if name:
        engine.say("Encantado de conocerte, {}.".format(name))

    else: 
        engine.say("no te entiendo una verga, sacate el dedo del culo")
    engine.runAndWait()



if __name__ == '__main__':
    main()


