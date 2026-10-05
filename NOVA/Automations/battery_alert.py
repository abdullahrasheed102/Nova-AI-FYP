import random
import time
import psutil
import os,sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Data.data.DLG import low_b, last_low, full_battery
from Body.Speak.Speak import Speak


def battery_alert():
    while True:
        time.sleep(10)
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent < 30:
            random_low = random.choice(low_b)
            Speak(random_low)

        elif percent < 10:
            random_low = random.choice(last_low)
            Speak(random_low)

        elif percent == 95:
            random_low = random.choice(full_battery)
            Speak(random_low)
        else:
            pass

        time.sleep(1500)

def battery_alert1():
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent < 30:
            random_low = random.choice(low_b)
            Speak(random_low)

        elif percent < 10:
            random_low = random.choice(last_low)
            Speak(random_low)

        elif percent == 95:
            random_low = random.choice(full_battery)
            Speak(random_low)
        else:
            Speak("sir,your battery is in perfect battery level")
