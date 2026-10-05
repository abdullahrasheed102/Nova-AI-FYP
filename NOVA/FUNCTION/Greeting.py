import os
import sys
import random
import datetime
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Body.Speak.Speak import Speak
# from Body.Speak.SpeakOnline import Speak
# from Body.Speak.SpeakOnline2 import Speak
# from Body.Speak.SpeakUrdu import Speak

from Data.data.DLG import good_morningdlg, good_afternoondlg, good_eveningdlg, good_nightdlg
today = date.today()
formatted_date = today.strftime("%d %b %y")
nowx = datetime.datetime.now()

def Greating():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        gd_dlg = random.choice(good_morningdlg)
        Speak(gd_dlg)
    elif 12 <= current_hour < 17:
        ga_dlg = random.choice(good_afternoondlg)
        Speak(ga_dlg)
    elif 17 <= current_hour < 21:
        ge_dlg = random.choice(good_eveningdlg)
        Speak(ge_dlg)
    else:
        gn_dlg = random.choice(good_nightdlg)
        Speak(gn_dlg)
    Speak('How can I assist you?')

# Greating()