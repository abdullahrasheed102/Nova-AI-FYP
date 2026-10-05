import psutil
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Body.Speak.Speak import Speak

def battey_persentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    Speak(f"the device is running on {percent}% battery power")