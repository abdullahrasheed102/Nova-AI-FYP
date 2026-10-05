# Built by Muhammad Abdullah Rasheed, Adil Hayyat and Jabran Adeel
# Standard library imports
import cv2
import os, sys
import random
import operator
import pygame
import pyautogui
import psutil
import pywhatkit as kit
import requests
import speech_recognition as sr
import tkinter as tk
import time
import webbrowser
import wikipedia
pygame.init()

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import DATA_DIR, GUI_DIR, MEMORY_DIR, MUSIC_DIR, PLAYLIST_DIR, SOUND_DIR, WALLPAPER_DIR
from FUNCTION.platform_utils import (
    APP_NAMES, get_active_window_title, get_brightness, hotkey, kill_app, open_app,
    open_path, play_sound as play_platform_sound, power_action, press_enter,
    press_key, scroll, set_brightness, set_wallpaper,
)

from bs4 import BeautifulSoup
from mtranslate import translate
from word2number import w2n
from time import sleep
from PIL import Image

from Body.Listen.ListenJs import Listen
from Body.Speak.Speak import Speak

from FUNCTION.Dictionary import *
from FUNCTION.DateTime import *
from FUNCTION.Quran import *
from FUNCTION.Map import *
from FUNCTION.Weather import *
from FUNCTION.Location import *
from FUNCTION.Wallpaper import *
from FUNCTION.PDFReader import *
from FUNCTION.system_info import *

try:
    from FUNCTION.News import News
except Exception as exc:
    print(f"Optional News module unavailable: {exc}")
try:
    from FUNCTION.jokes import *
except Exception as exc:
    print(f"Optional jokes module unavailable: {exc}")
try:
    from FUNCTION.pdf import *
except Exception as exc:
    print(f"Optional PDF module unavailable: {exc}")
try:
    from FUNCTION.Wifi import *
except Exception as exc:
    print(f"Optional Wi-Fi module unavailable: {exc}")
try:
    from FUNCTION.Reminders.notify import *
except Exception as exc:
    print(f"Optional reminders module unavailable: {exc}")
try:
    from FUNCTION.DataOnline import Online_Scraper
except Exception as exc:
    print(f"Optional online data module unavailable: {exc}")
try:
    from FUNCTION.NewsRead import get_user_preference
except Exception as exc:
    print(f"News data unavailable; news commands are disabled: {exc}")
try:
    from FUNCTION.Graph_Visualizer.application import *
except Exception as exc:
    print(f"Optional graph visualizer unavailable: {exc}")
try:
    from FUNCTION.PDF_AudioBook.pdf import *
except Exception as exc:
    print(f"Optional PDF audio module unavailable: {exc}")

from Automations.open import opened
from Automations.battery_alert import *
from Automations.battery_plug_check import *
from Automations.check_battery_persentage import *
try:
    from Generate.Imagegen import generate_image
    from Generate.Mistral2 import generate_code
except Exception as exc:
    print(f"Image and code generation unavailable: {exc}")

    def generate_image(description):
        print("Image generation is unavailable because its optional module is missing.")

    class _UnavailableCodeGenerator:
        def Mistral7B(self, query):
            return "Code generation is unavailable because its optional module is missing."

    def generate_code():
        return _UnavailableCodeGenerator()
try:
    from Brain.Osrc.Chat import Chat
except Exception as exc:
    print(f"Chat module unavailable; conversational chat is disabled: {exc}")

    def Chat(query):
        return ("Chat is unavailable because its optional module is missing.", 0.0)
from Data.data.DLG import *

global random_song
random_song = None  



# Functions ################################################################################################################################

def scroll_down():
    scroll(-3)

def scroll_up():
    scroll(3)

def press_enter_key():
    press_enter()

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def battery():
    battery = psutil.sensors_battery()
    battery_percentage = str(battery.percent)
    plugged = battery.power_plugged
    Speak(f"Sir, it is {battery_percentage} percent.")
    if plugged:
        Speak("and It is charging....")
    if not plugged:
        if battery_percentage <= "95%":
            Speak("Sir, plug charger.")

def play_sound(file_path):
    if not os.path.isfile(file_path):
        print(f"Sound file unavailable; skipping playback: {os.path.basename(file_path)}")
        return
    play_platform_sound(file_path)


# Plays a video on YouTube
def play_on_youtube(video):
    kit.playonyt(video)

# Searches Google
def search_on_google(query):
    kit.search(query)


def take_picture(output_filename):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        Speak("Error: Unable to open camera.")
        return
    ret, frame = cap.read()
    if not ret:
        Speak("Error: Unable to capture frame.")
        cap.release()
        return
    save_path = os.path.join(MEMORY_DIR, output_filename)
    cv2.imwrite(save_path, frame)
    cap.release()

def show_random_image_from_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        # Filter image files (e.g., JPG, PNG)
        image_files = [file for file in files if file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
        if not image_files:
            Speak("No image files found in the specified folder.")
            return
        image_file = random.choice(image_files)
        img_path = os.path.join(folder_path, image_file)
        img = Image.open(img_path)
        img.show()
        time.sleep(2)
    except IOError:
        Speak("Sorry, unable to display the picture.")


# OpenApps ###################################################################################################################################

# Chatbot ###################################################################################################################################

# Define the possible greetings and responses
reply_greetings = ["Hello Sir,welcome back",
                   "Hey, what's up?",
                   "Hello Sir",
                   "Hello Sir, nice to meet you again.",
                   "Hello! How can I assist you sir",
                   "Of course Sir, hello."]

# Define the possible farewells and responses
reply_farewells = ["Rest mode activated, Wake me when needed",
                   "Bye Sir.",
                   "It's okay.",
                   "It will be nice to meet you.",
                   "Bye sir, the computer is going to sleep mode",
                   "Thanks.",
                   "Okay."]

# Define the possible inquiries about well-being and responses
inquiries = ('how are you', 'are you fine')
reply_inquiries = ("I am fine Sir, Tell me, Hoe can I assist you",
                   "Excellent, Sir.",
                   "Good, maza lga hova hn",
                   "Absolutely fine.",)

# Define the possible positive expressions and responses
positives = ('nice', 'thanks')
reply_positives = ("Thanks.",
                   "Ohh, it's okay.",
                   "Thanks to you.")

# Ask about introduction and responses
intro = ['who create you', 'who created you', 'who made you', 'who are you']
reply_intro = ("I am Nova AI, built by Muhammad Abdullah Rasheed, Adil Hayyat and Jabran Adeel.",)

# Define the possible inquiries about functions/features and responses
inquiries = ['what you can do', 'abilities', 'features', 'whats you can do']
reply_inquiries = ("I can perform many tasks like image generation, code generation, pdf reading, chatting and much more. How can I help you?",
                            "I can chat with you, tell the time and date, search on Google, Wikipedia and YouTube, turn apps on and off, write note for you,  generate images and code, and much more")


# OPENING COMMANDS ######################################################################################################################

def Respond():         
    while  True:
        query = Listen().lower()           
        query = translate(query, 'en', 'auto')

        CURRENT_APP=""
        try:
            CURRENT_APP = get_active_window_title()
        except :
            CURRENT_APP = ""
        # CURRENT_APP NAME
        # CURRENT_APP_NAME=CURRENT_APP.split(" - ")[-1]

        if any(word in query for word in ["generate", "image"]):
            text = query[len("generate"):].strip()
            text = query[len("image"):].strip()
            generate_image(text)

        elif any(word in query for word in ["code", "script"]):
            generated_code = generate_code()
            response = generated_code.Mistral7B(query)
            print(response)
            Speak('Code generated successfully Sir')

        elif any(word in query for word in ["poem"]):
            generated_code = generate_code()
            response = generated_code.Mistral7B(query)
            print(response)
            Speak('poem generated successfully Sir')

        elif any(word in query for word in ["recommend", "recommendation"]):
            generated_code_info = generate_code() 
            response = generated_code_info.Mistral7B(query)
            print(response)
            Speak("Here is the recommandations sir, read it")

        elif any(word in query for word in ["advise", "analysis", "health"]):
            generated_code_info = generate_code() 
            response = generated_code_info.Mistral7B(query)
            print(response)
            Speak("Here are the instructions, sir. You can read...")


        # elif any(word in query for word in ["read pdf", "open pdf reader",  "pdf"]):
        #     root = tk.Tk()
        #     root.bbox("750x750")  
        #     pdf_reader = PDFReader(root)
        #     pdf_reader.start_voice_recognition()  # Start listening for voice commands
        #     root.mainloop()

        elif any(word in query for word in ["read pdf", "open pdf reader",  "pdf"]):
            main_pdf()
            
        # Trigonometric ratios graph visualizer
        elif any(word in query for word in ["graph visualizer", "open graph visualizer", "open graph", "graph", "open graph view liser"]):
            Speak("Opening Trigonometric ratios graph visualizer, Sir")
            root = tk.Tk()
            root.bbox('800x620')
            root.wm_title('Graph Visualizer')
            app = Application(master=root)
            app.mainloop()


        elif any(word in query for word in ["reminder", "open reminder",  "set reminder"]):
            run_reminder_app()

# CHAT WITH NOVA AI ############################################################################################################################

# CHAT WITH NOVA AI ############################################################################################################################

        elif any(word in query for word in reply_greetings):
            greeting = random.choice(reply_greetings)
            Speak(greeting)

        elif any(word in query for word in inquiries):
            Speak(random.choice(reply_inquiries))

        elif any(word in query for word in positives):
            Speak(random.choice(reply_positives))

        elif any(word in query for word in inquiries):
            Speak(random.choice(reply_inquiries))

        elif any(word in query for word in intro):
            Speak(random.choice(reply_intro))


        elif ("what's your name" in query):
            Speak("I am Nova AI, built by Muhammad Abdullah Rasheed, Adil Hayyat and Jabran Adeel.")

        elif "how old are you" in query:
            Speak("I am 20 years old sir")

        elif "how are you" in query:
            Speak("Thank you for asking, I'm here to assist you in any way I can, what about you, sir")

        elif "I'm good" in query or "I am good" in query:
            Speak("Nice to hear that, sir")

        elif "what is this behaviour" in query:
            Speak("what happened, calm down, sir!")
            
        elif any(word in query for word in [ "Okay", "Ok"]): 
            Speak("Alright! sir")

        elif "whats your nickname" in query or "what's your nickname" in query:
            Speak("My nickname is jarko")

        elif "do you have a family" in query or "do you have family" in query:
            Speak("No, I only have father")

        elif "who is your father" in query:
            Speak("Haroon is my father")

        elif "who is your developer" in query or "who is your creater" in query:
            Speak("Adil Hayat and company developed me")

        elif "do you have a girlfriend" in query or "do you have a girlfriend" in query or "do you have girlfriend" in query:
            Speak("I don't have a girlfriend; I'm single. But I have a crush on Friday.")

        elif "whats your nickname" in query or "what's your nickname" in query  or "your nickname" in query:
            Speak("My nickname is Jarko")   

        elif "which languages can you speak" in query or "which languages you can speak" in query:
            Speak("I can speak almost all languages but you have to design me for English")


# OPEN/CLOSE #################################################################################################################################
        
        elif 'home screen' in query:
            hotkey('win', 'm')

        elif 'back to previous screen' in query or 'previous screen' in query  or 'open previous screen' in query:
            hotkey('alt', 'tab')


        elif "click refresh" in query:
            pyautogui.moveTo(1636,236, 2)
            pyautogui.click(x=1636, y=236, clicks=1, interval=0, button='right')
            pyautogui.moveTo(1376,308, 1)
            pyautogui.click(x=1376, y=308, clicks=1, interval=0, button='left')

        elif "refresh" in query or "refresh page" in query:
            press_key("f5")  # Refresh the current browser page
            Speak("Refreshing the page")

        elif 'open setting' in query:
            open_app("settings")
            

    # WEBSITS -------------------------------------------------------------------------------------------------------------------------

        elif "open google" in query:
            webbrowser.open("www.google.com")
            Speak("Opening Google")
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            Speak("Opening YouTube")
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
            Speak("Opening Facebook")
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
            Speak("Opening instagram")
        elif "open github" in query or "git hub" in query or "get hub" in query:
            webbrowser.open("https://www.github.com")
            Speak("Opening GitHub")
        elif "open twitter" in query or "open x" in query:
            webbrowser.open("https://www.twitter.com")
            Speak("Opening Twitter, I mean X")
        elif "open linkedin" in query:
            webbrowser.open("https://www.linkedin.com")
            Speak("Opening LinkedIn")
        elif "open microsoft office" in query or "open office" in query:
            webbrowser.open("https://www.office.com")
            Speak("Opening Microsoft Office")
        elif "open stackoverflow" in query or "open stack overflow" in query:
            webbrowser.open("https://www.stackoverflow.com")
            Speak("Opening Stack Overflow")

        elif "open islamia university" in query or "open world class university" in query:
            webbrowser.open("https://www.iub.edu.pk/")
            Speak("Opening world class university, The Islmaia university")

        elif "open harvard university" in query or "harvard university" in query:
            webbrowser.open("https://online.hbs.edu/")
            Speak("Opening harvard university, Sir")

        elif "open Oxford university" in query or "Oxford university" in query:
            webbrowser.open("https://www.ox.ac.uk/")
            Speak("Opening University of Oxford, Sir")


    # WINDOW -----------------------------------------------------------------------------------------------------------------------------

        elif any(word in query for word in [ "minimise window" ,  "window minimize" , "minimise this window"]):
            hotkey("win", "down")
            Speak("Ok sir")

        elif any(word in query for word in [ "maximize window" , "maximise window", "maximise this window", "maximize this window"]):
            hotkey("win", "up")
            Speak("Ok sir")

        elif "change window" in query or "change the window" in query:
            hotkey("alt", "tab")
            Speak("Ok sir")

        elif "close window" in query or "close the window" in query:
            hotkey("alt", "f4")
            Speak("Ok sir")

        elif 'open new window' in query or 'open new tab' in query:
            hotkey('ctrl', 'n')

        elif 'open next tab' in query or 'next tab' in query:
            hotkey('ctrl', 'tab')

        elif 'open previous tab' in query or 'previous tab' in query:
            hotkey('ctrl', 'shift', 'tab')

        elif 'open incognito window' in query:
            hotkey('ctrl', 'shift', 'n')

        elif 'open history' in query:
            hotkey('ctrl', 'h')

        elif 'open downloads' in query:
            hotkey('ctrl', 'j')

        elif 'close tab' in query:
            hotkey('ctrl', 'w')

        elif "press the" in query and "button" in query:
            button = query.replace("press the ", "")
            button = button.replace(" button", "")
            press_key(button)
            Speak("Ok sir")

        elif "open browser menu" in query:
            hotkey('alt', 'f')
            Speak("Opening Browser Menu")

        elif "open task manager" in query:
            hotkey("ctrl", "shift", "esc")
            Speak("Opening task manager sir")

        elif "open taskview" in query or "open task view" in query:
            hotkey("win", "tab")
            Speak("Opening Task View")
            time.sleep(1)  # Adjust the delay as needed
            Speak("Which task do you want to open, sir?")
            task_query = Listen().lower()
            # Wait for the user to make a selection (adjust the delay as needed)
            time.sleep(3)
            # Dictionary to map task keywords to their coordinates
            task_coordinates = {
                "open first": (214, 306),
                "open second": (648, 306),
                "open third" : (1070, 306),
                "open four"  : (272, 571),
                "open five"  : (672, 571),
                "open six"   : (1125, 571)
            }
            # Simulate the click on the selected task if the keyword matched
            if task_query.lower() in task_coordinates:
                x, y = task_coordinates[task_query.lower()]
                pyautogui.moveTo(x, y, duration=0.2)  # Faster cursor movement
                pyautogui.click(x, y)  # Quick click
                Speak("Opening the selected task")
            else:
                Speak("Sorry, I couldn't understand your selection.")

        elif "open on screen keyboard" in query or "open screen keyboard" in query :
            hotkey("win", "ctrl", "o")  # Open On-Screen Keyboard
            Speak("Opening On-Screen Keyboard")

        elif "close on screen keyboard" in query or "close screen keyboard" in query :
            hotkey("win", "ctrl", "o")  # Open On-Screen Keyboard
            Speak("Closing On-Screen Keyboard")

        elif 'clear browsing history' in query:
            hotkey('ctrl', 'shift', 'delete')

        # CLOSE --------------------------------------------------------------------------------------------------------------------

        elif "close" in query or "bnd krdo" in query:  # assuming this is your elif statement
            closedlg_random = random.choice(closedlg)
            Speak(closedlg_random)
            hotkey("alt","f4")

        elif "close browser" in query:
            kill_app("msedge.exe")
            Speak("Web browser is closing sir")

        elif 'close chrome' in query :
            kill_app("chrome.exe")
            Speak("chrome is closing sir")


# SEARCH ################################################################################################################################

        elif 'search' in query and 'on google' in query:
            article = query.replace('search', '').replace('on google', '').strip()
            Speak('searching {} on google, Sir'.format(article))
            search_on_google(article)

        elif "search google" in query:
            # Check if the query is just "search" or contains additional keywords
            if query.strip() == "search google":
                Speak("What should I search on Google? ")
                search_query = Listen().lower()  # Get user's input for the search
                search_query = translate(search_query, 'en', 'auto')  # Translate the query
            else:
                # Extract the search query from the user's input
                search_query = query.replace("search", "").strip()
                search_query = translate(search_query, 'en', 'auto')  # Translate the query

            # Perform a Google search using the search_query
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(search_url)
            Speak('searching {} on google'.format(search_query))  # Corrected 'article' to 'search_query'


        elif "search on youtube" in query:
            youtube_Search_URL = "https://www.youtube.com/results?search_query="
            try:
                if query == "search on youtube":
                    Speak("What do you want me to search sir")
                    search = Listen()
                    url = youtube_Search_URL + search
                    dlg = random.choice(yt_search)
                    Speak(dlg)
                else:
                    search = query.replace("on youtube", "")
                    search2 = search.replace("search", "")
                    url = youtube_Search_URL + search2

                webbrowser.open(url)
                Speak("searching" + search)
            except:
                Speak("I don't understand sir")

        elif 'play' in query and 'on youtube' in query:
            yousearch = query.replace('play', '').replace('on youtube', '').strip()
            Speak('playing {} on YouTube, Sir'.format(yousearch))
            play_on_youtube(yousearch)

        elif "according to wikipedia" in query:
            query = query.split("according to wikipedia")[1].strip()
            try:
                result = wikipedia.summary(query, sentences=2)
                Speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                Speak(f"There were multiple matches for '{query}'. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                Speak(f"Sorry, there were no results found for '{query}'.")
            except Exception as e:
                Speak("I'm sorry, I couldn't process your request.")


        elif any(word in query.lower() for word in ["what is", "who is", "where is", "why", "which", "the", "The", "when"]):
            Speak(Online_Scraper(query))

# IMPORT FUNCTIONS #####################################################################################################################

        # JOKES ------------------------------------------------------------------------------------------------------------

        elif 'tell me joke' in query or "tell me cool joke" in query:   
             tell_joke()


        elif 'joke in Urdu' in query or "tell me any joke" in query or "tell something funny" in query or "latifa sunao" in query :
            tell_urdu_joke()

        # MAP LOCATION ------------------------------------------------------------------------------------------------------

    # Function to open the location on map goes here

        elif "open location of" in query and "on map" in query:
            location = query.replace('open location of', '').replace('on map', '').strip()
            Speak('Opening {} on map, Sir'.format(location))
            open_location_on_map(location)

        elif 'location' in query or "open location of" in query or "location of" in query:
            location = query.replace('location', '').replace('on map', '').strip()
            Speak('Opening {} on map, Sir'.format(location))
            open_location_on_map(location)

        # Dictionary -------------------------------------------------------------------------------------------------------

        elif any(word in query for word in ["meaning"]):
            word = query.split()[-1]
            Dict_Meanings(word)

        elif any(word in query for word in ["synonyms"]):
            word = query.split()[-1]
            Dict_Synonyms(word)

        # Wifi ------------------------------------------------------------------------------------------------------------

        elif "Wi-Fi" in query and "on" in query:
            turn_wifi_on()
            Speak("Wi-Fi turned on!")

        elif "Wi-Fi" in query and "off" in query:
            turn_wifi_off()
            Speak("Wi-Fi turned off!")

        # News -------------------------------------------------------------------------------------------------------------

        elif 'tell me news' in query or "aaj ki news sunao" in query or "today's news" in query:
            Speak(News())

        # elif 'tell me news' in query or "aaj ki news sunao" in query or "today's news" in query:
        elif any(word in query for word in ["news", "current news"]) :
            get_user_preference()

        # Calculate -------------------------------------------------------------------------------------------------------------

        elif any(word in query for word in ["calculate"]):
            r = sr.Recognizer()
            with sr.Microphone(device_index=0) as source:
                r.energy_threshold = 3500
                r.dynamic_energy_threshold = True
                Speak("What calculation you want?")
                print("Listning...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, phrase_time_limit=15)
                my_string=r.recognize_google(audio) 
                print(my_string)

            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    '/' : operator.truediv,  
                    '*' : operator.mul,       
                }[op]
             
            def eval_binary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            Speak("your result is")
            Speak(eval_binary_expr(*(my_string.split())))

# CLOCK/TEMP ###########################################################################################################################

        elif 'time' in query or "time kya hua" in query or "Whats time now" in query:
            time_Tell()

        elif "date" in query or "aaj date kya hai" in query or "Whats date today" in query  or "Whats date" in query  or "date today" in query:
                Speak("Today's date is " + get_today_date())

        elif "din" in query or "aaj kya din hai " in query or "today" in query:
            Speak("Today is " + get_today_day())

        #for telling weather of the required city
        elif "how's weather in" in query or "temperature in" in query or "how is weather in" in query or "whats temperature in" in query:
            city = query.split("in")[-1].strip()
            weather_report = weather(city)
            Speak(weather_report)

        #for telling weather of the current city
       
        elif "how's weather now" in query or "what's weather now" in query  or "what's temperature" in query or "what's temperature now" in query:
            city = "Bahawalpur"
            weather_report = weather(city)
            Speak(weather_report)


# BRIGHTNESS ################################################################################################################################ 

        elif "increase brightness" in query or "raise brightness" in query or "brightness up" in query:
            max_brightness = 100
            increased = False
            for display_index in range(len(get_brightness())):
                current_brightness = get_brightness()[display_index]
                new_brightness = min(max_brightness, current_brightness + 10)  # Increase brightness by 10%
                if new_brightness > current_brightness:
                    increased = True
                    set_brightness(new_brightness, display=display_index)
                    Speak(f"Screen brightness increased to {new_brightness}%")
            if not increased:
                Speak("Your screen brightness is already at its highest level.")

        elif "decrease brightness" in query or "reduce brightness" in query or "brightness down" in query:
            max_brightness = 100
            decreased = False
            for display_index in range(len(get_brightness())):
                current_brightness = get_brightness()[display_index]
                new_brightness = max(0, current_brightness - 10)  # Decrease brightness by 10%
                if new_brightness < current_brightness:
                    decreased = True
                    set_brightness(new_brightness, display=display_index)
                    Speak(f"Screen brightness decreased to {new_brightness}%")
            if not decreased:
                Speak("Your screen brightness is already at its lowest level.")


        elif "set screen brightness to" in query:
            brightness_value_str = query.split("set screen brightness to")[-1].strip()
            try:
                brightness_value = int(brightness_value_str)
                if 0 <= brightness_value <= 100:
                    for display_index in range(len(get_brightness())):
                        set_brightness(brightness_value, display=display_index)
                    Speak(f"Screen brightness set to {brightness_value}%")
                else:
                    Speak("Brightness value should be between 0 and 100")
            except ValueError:
                Speak("Invalid brightness value. Please provide a number between 0 and 100.")

        elif "set brightness to" in query:
            brightness_value_str = query.split("set brightness to")[-1].strip()
            try:
                brightness_value = int(brightness_value_str)
                if 0 <= brightness_value <= 100:
                    for display_index in range(len(get_brightness())):
                        set_brightness(brightness_value, display=display_index)
                    Speak(f"Screen brightness set to {brightness_value}%")
                else:
                    Speak("Brightness value should be between 0 and 100")
            except ValueError:
                Speak("Invalid brightness value. Please provide a number between 0 and 100.")

# MEDIA ################################################################################################################################ 

        # To open camera
        elif "open camera" in query:
            opened(query)

        # To take Picture
        elif "take my Picture" in query or "click my Picture" in query or "click my image" in query or "click photo" in query:
            take_picture("captured_image.jpg")
            Speak("Picture Clicked and Saved in Memory Folder successfully")

        elif "show me the Picture" in query or "show me photo" in query or "show photo" in query:
            folder_path = MEMORY_DIR  # Change this to your desired folder path
            show_random_image_from_folder(folder_path)
            Speak("Here is the picture, sir")

        # To take screenshot
        elif "take screenshot" in query or "take a screenshot" in query or "capture the screen" in query:
            img = pyautogui.screenshot()
            desktop_path = os.path.join(os.path.expanduser("~"), "Pictures", "Screenshots")
            if not os.path.exists(desktop_path):
                os.makedirs(desktop_path)
            img_path = os.path.join(desktop_path, "screenshot.png")
            img.save(img_path)
            Speak("Screenshot captured successfully sir")

        elif "show me the screenshot" in query or "show me screenshot" in query:
            try:
                img_path = os.path.join(os.path.join(os.path.expanduser("~"), "Pictures", "Screenshots"), "screenshot.png")
                img = Image.open(img_path)
                img.show()  # Removed img parameter
                time.sleep(2)
                Speak("Here is the screenshot, sir")
            except IOError:
                Speak("Sorry sir, I am unable to display the screenshot")

        # To write the note on notepad
        elif "take a note" in query:
            Speak("What would you like the file name to be, sir?")
            nameFile = Listen() + ".txt"
            Speak("What do you want to record, sir?")
            textFile = Listen()
            home_directory = os.path.expanduser("~")
            file_path = os.path.join(MEMORY_DIR, nameFile)     
            # Open the file for writing
            with open(file_path, "w") as file:
                file.write(textFile)     
            Speak("The file saved successfully in Folder named, Nova AI Memory.")

        elif "show me the note" in query or "show me note" in query:
            Speak("Sure, sir. What is the name of the file?")
            file_name = Listen() + ".txt"
            home_directory = os.path.expanduser("~")
            file_path = os.path.join(MEMORY_DIR, file_name)
            try:
                with open(file_path, "r") as file:
                    note_content = file.read()
                    Speak("Here is the content of the note:")
                    Speak(note_content)
            except FileNotFoundError:
                Speak("Sorry, I couldn't find the specified note. Please make sure the file name is correct.")

        # To play the surah of Holy Quran
        elif "play surah" in query or "start surah" in query or "play surat" in query or "play surat" in query:
            play_surah(query)

        elif any(word in query for word in ["stop music", "start music", "start video" , "stop video", "hold"]):
            press_key("playpause")
            Speak("Okay sir")

        elif "play music" in query or "hit some music" in query:
            music_dir = MUSIC_DIR
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            open_path(os.path.join(music_dir, random_song))
            Speak("playing music sir")

        # To play the next music
        elif "play next music" in query or "next music" in query:
            # Assuming songs is a list of your songs
            current_song_index = songs.index(random_song)
            next_song_index = (current_song_index + 1) % len(songs)  # This will loop back to the first song if we're at the end
            next_song = songs[next_song_index]
            open_path(os.path.join(music_dir, next_song))
            Speak("playing next music sir")

        # To play the previous music
        elif "play previous music" in query or "previous music" in query:
            current_song_index = songs.index(random_song)
            prev_song_index = (current_song_index - 1) % len(songs)  # This will loop back to the last song if we're at the start
            prev_song = songs[prev_song_index]
            open_path(os.path.join(music_dir, prev_song))
            Speak("playing previous music sir")

        # Inside the "play video" elif block
        elif "play video music" in query or "play video" in query:
            music_dir = PLAYLIST_DIR
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            open_path(os.path.join(music_dir, random_song))
            Speak("playing video sir")

        # Inside the "play next video" elif block
        elif "play next video" in query or "next video" in query:
            current_song_index = songs.index(random_song)
            next_song_index = (current_song_index + 1) % len(songs)
            random_song = songs[next_song_index]
            open_path(os.path.join(music_dir, random_song))
            Speak("playing next video sir")

        # Inside the "play previous video" elif block
        elif "play previous video" in query or "previous video" in query:
            current_song_index = songs.index(random_song)
            prev_song_index = (current_song_index - 1) % len(songs)
            random_song = songs[prev_song_index]
            open_path(os.path.join(music_dir, random_song))
            Speak("playing previous video sir")


        elif "change wallpaper" in query or "swap wallpaper" in query or "change walpaper" in query:
            folder_path = WALLPAPER_DIR
            random_image = get_random_image_from_folder(folder_path) 
            change_wallpaper(random_image)
            Speak("wallpaper changed successfully")

        elif "activate auto wallpaper" in query or "start auto wallpaper" in query:
            Speak("Auto wallpaper activating, Please wait Sir")
            folder_path = WALLPAPER_DIR
            change_interval = 60  
            random_image = get_random_image_from_folder(folder_path) 
            change_wallpaper(random_image)
            time.sleep(change_interval)
            Speak("Auto wallpaper changing activated, Sir")


# Volume ############################################################################################################################

        elif "scroll down" in query or "down scroll" in query:
            scroll_down()

        elif "scroll up" in query  or "up scroll" in query or "scroll" in query:
            scroll_up()

        elif "press enter button" in query or "press enter" in query:
            press_enter_key()

        elif "pause" in query or "stop video" in query:
            press_key("k")
            Speak("video paused")

        elif any(word in query for word in ["volume up", "increase volume", "volume increase"]):
            if "by" in query:  # Check if a specific volume level is mentioned
                try:
                    # Extract the desired volume level from the query
                    level = int(query.split("by")[-1].strip())
                    realLevel = level / 2  # Adjust the volume level as needed
                    press_key("volumeup", presses=int(realLevel))
                    Speak(f"Volume increased by {level}")
                except:
                    Speak("I don't understand sir")
            else:
                # If no specific volume level is mentioned, increase volume by default
                press_key("volumeup")
                press_key("volumeup")
                press_key("volumeup")
                press_key("volumeup")
                press_key("volumeup")
                Speak("Volume increased.")

        elif any(word in query for word in ["volume down", "decrease volume", "volume decrease", "reduce volume"]):
            if "by" in query:  # Check if a specific volume level is mentioned
                try:
                    # Extract the desired volume level from the query
                    level = int(query.split("by")[-1].strip())
                    realLevel = level / 2  # Adjust the volume level as needed
                    press_key("volumedown", presses=int(realLevel))
                    Speak(f"Volume decreased by {level}")
                except:
                    Speak("I don't understand sir")
            else:
                # If no specific volume level is mentioned, decrease volume by default
                press_key("volumedown")
                press_key("volumedown")
                press_key("volumedown")
                press_key("volumedown")
                press_key("volumedown")
                Speak("Volume decreased.")

        elif any(word in query for word in ["mute"]):
            press_key("volumemute")
            Speak("Volume muted.")

        elif "exit" in query:
            Speak("Exiting volume control.")

# OPEN APPS ##########################################################################################################################

        elif "open" in query:
            if ".com" in query or ".co.in" in query or ".org" in query or ".edu" in query or ".in" in query:
                query = query.replace("open","")
                query = query.replace("launch","")
                query = query.replace(" ","")
                webbrowser.open(f"https://www.{query}")
                Speak(f"Launching {query}, Sir!") 
            else:
                for app in APP_NAMES:
                    if app in query:   
                        open_app(app) 
                        query = query.replace("open","")   
                        Speak(f"Launching {query}, Sir!") 

# SOUND EFFECTS #########################################################################################################################

        elif any(word in query for word in [ "haha" , "he he" , "just laugh", "hanso", "laugh"]):
            play_sound(os.path.join(SOUND_DIR, "laugh.mp3"))

        elif "welcome" in query or "welcome nova" in query or "welcome back" in query:
            print('welcome back sir...')
            play_sound(os.path.join(SOUND_DIR, "open.mp3"))

        elif "introduce nova" in query or "intro please" in query or "tell about yourself" in query or "introduce about yourself" in query:
            print("Allow me to introduce myself. I am Nova AI, built by Muhammad Abdullah Rasheed, Adil Hayyat and Jabran Adeel. I am here to assist you with a variety of tasks.")
            play_sound(os.path.join(SOUND_DIR, "open2.mp3"))
            
# COMPUTER PC ##########################################################################################################################

        elif "give me system reports" in query or "system reports" in query or "system status" in query or "system report" in query:
            system_info = get_system_info()
            Speak(f"All systems are activated at {system_info}, Everything looks great!")

        elif "check battery percentage" in query or "battery percentage" in query:
            battey_persentage()
        elif "check the plug" in query or "check battery plug" in query:
            check_plugin_status1()
        elif "give me the battery alert" in query or "battery alert" in query:
            battery_alert1()
        elif "battery check" in query or "power check" in query or  "check battery" in query:
            battery()

        elif any(word in query for word in ["ip address"]):

                ip_address = find_my_ip()
                Speak(
                    f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
                print(f'Your IP Address is {ip_address}')

        elif "shut down the computer" in query or "shut down the pc" in query:
            Speak("Ok sir the computer is shutting down")
            power_action("shutdown")

        elif "log off" in query:
            power_action("logout") # log off computer

        elif "restart the computer" in query or "restart the pc" in query:
            Speak("Ok sir the computer is restarting")
            power_action("restart")

        elif  "sleep the computer system" in query or "Lock the system" in query:
            Speak("Ok sir the computer is going to sleep mode")
            power_action("sleep")

        elif "sleep nova" in query or "rest nova" in query or "bye nova" in query:
            farewell_message = random.choice(reply_farewells)
            Speak(farewell_message)
            sys.exit()

        elif query.lower().startswith('nova ') or Chat(query)[1] > 0.99 or Chat(query)[1] > 0.99:
            try:
                response, _ = Chat(query) 
                Speak(response)
            except (KeyboardInterrupt, EOFError, SystemExit):
                break

        else:
            try:
                response, _ = Chat(query) 
                Speak(response)
            except (KeyboardInterrupt, EOFError, SystemExit):
                break


###########################################################################################################################################

# def time_input():
#     global timeInput
#     timeInput = input("Enter time within 8 seconds: ")

# def pdf_input():
#     global pdfInput
#     pdfInput = input("Enter pdf within 8 seconds: ")

############################################################################################################################################




# Respond() 
