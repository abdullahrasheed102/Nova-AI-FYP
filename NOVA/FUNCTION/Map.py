import webbrowser
import time
import pyautogui as gui
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from FUNCTION.platform_utils import press_enter
from Body.Speak.Speak import Speak

def open_location_on_map(location):
    webbrowser.open("https://www.google.com/maps/@16.3524328,79.8664982,16196013m/data=!3m1!1e3")
    time.sleep(8)
    gui.write(location)
    Speak("searching.")
    press_enter()
    Speak(f"Here is the {location}, sir")

# if __name__ == "__main__":
#     query = "open location of Paris on map"  # Example query for testing

#     if "open location of" in query and "on map" in query:
#         location = query.replace('open location of', '').replace('on map', '').strip()
#         Speak('Opening {} on map, Sir'.format(location))
#         open_location_on_map(location)
#     elif 'location' in query or "open location of" in query or "location of" in query:
#         location = query.replace('location', '').replace('on map', '').strip()
#         Speak('Opening {} on map, Sir'.format(location))
#         open_location_on_map(location)
