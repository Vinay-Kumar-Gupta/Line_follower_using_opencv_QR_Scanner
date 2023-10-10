import pyttsx3
from threading import Thread
# ======================================== Voice Setup =====================================
voice = pyttsx3.init()

flag = False

def speak_config(voice_rate ,voice_id):
    voice.setProperty("rate", voice_rate)
    voices = voice.getProperty("voices")
    voice.setProperty("voice", voices[voice_id].id)

def speak(text):
    global flag
    try :
        flag = True
        voice.say(text)
        voice.runAndWait()
        flag = False
        voice.stop()

    except RuntimeError as r:
        pass

def status():
    global flag
    return flag




