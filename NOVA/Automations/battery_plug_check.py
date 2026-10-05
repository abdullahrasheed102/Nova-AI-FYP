import random
import psutil
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Data.data.DLG import plug_out, plug_in
from Body.Speak.Speak import Speak


def check_plugin_status():
    battery = psutil.sensors_battery()
    previous_state = battery.power_plugged

    while True:
        battery = psutil.sensors_battery()

        if battery.power_plugged != previous_state:
            if battery.power_plugged:
              random_low = random.choice(plug_in)
              Speak(random_low)
            else:
              random_low = random.choice(plug_out)
              Speak(random_low)

            previous_state = battery.power_plugged

previous_state = None
plug_in1 = ["charger is plugged check conform", "battery is charging that means charger is plugged check completed"]
plug_out1 = ["Charger status unplugged", "battery is not charging that means charger is not plugged check completed"]
def check_plugin_status1():
    global previous_state  # Use the global variable

    battery = psutil.sensors_battery()

    if battery.power_plugged != previous_state:
        if battery.power_plugged:
            random_low = random.choice(plug_in1)
            Speak(random_low)  # Assuming speak function is defined
        else:
            random_low = random.choice(plug_out1)
            Speak(random_low)  # Assuming speak function is defined

        previous_state = battery.power_plugged