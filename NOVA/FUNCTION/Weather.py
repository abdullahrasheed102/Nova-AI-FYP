import os
import sys
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

# Assuming Listen and Speak are correctly imported from the paths provided
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Body.Listen.ListenJs import Listen
from Body.Speak.Speak import Speak

def weather(city):    
    url = f"https://www.google.com/search?q=weather+{city}"
    html = requests.get(url).content
    soup = BeautifulSoup(html, "lxml")
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    details = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text.split('\n')
    time = details[0]
    sky = details[1] 
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
    pos = strd.find('Wind')
    other_data = strd[pos:]
    result = f'The temperature in {city} is currently {temp.replace("C", "Celsius")} and the sky is {sky} now'
    return result


# def main():
#     query = Listen().lower()
#     if "weather in" in query:
#         city = query.split("in")[-1].strip()
#         weather_report = weather(city)
#         Speak(weather_report)

# if __name__ == "__main__":
#     main()