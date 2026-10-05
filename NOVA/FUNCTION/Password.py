import speech_recognition as sr
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Body.Listen.ListenJs import Listen
from Body.Speak.Speak import Speak

def Password(pass_inp):
    password = os.environ.get("NOVA_PASSWORD", "").strip()
    if not password:
        password_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "Data",
            "password.txt",
        )
        try:
            with open(password_file, encoding="utf-8") as file:
                password = file.readline().strip()
        except OSError:
            password = ""

    if not password:
        print("No password configured. Set NOVA_PASSWORD or create NOVA/Data/password.txt")
        Speak("Access Not Granted. Please provide the correct password.")
        return False

    if pass_inp == password:
        Speak("Access Granted.")
        return True
    else:
        Speak("Access Not Granted. Please provide the correct password.")
        return False

# if __name__ == "__main__" :
#        Speak("Kindly Provide The Password To Access .")
#        pas = Listen()
#        Password(pas)
