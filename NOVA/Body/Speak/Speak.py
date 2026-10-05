import os
import sys
import pyttsx3
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from time import sleep
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from FUNCTION.platform_utils import create_tts_engine


engine = create_tts_engine()
voices = engine.getProperty('voices')

engine.setProperty('rate', 180)
if voices:
    engine.setProperty('voice', voices[0].id)


def Speak(*args, **kwargs):
    
    audio = ""
    for i in args:
        audio += str(i)
        # print(Fore.CYAN+audio)
        print(audio)

        engine.say(audio)
        engine.runAndWait()

# Speak("Hello how are you")
