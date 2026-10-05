import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Body.Speak.Speak import Speak
from datetime import datetime

#time_Tell() function tells time in 'HOURS' and 'MINUTES' with 'AM/PM'
#Time in 12Hour formate------------------------------------------------------------- 
def time_Tell():
    time_call = datetime.now()
    tick = (datetime.now())

    if time_call.hour>=0 and time_call.hour<=1:
        Speak(f'It is 12 and {time_call.minute} minute AM')
    elif time_call.hour>=1 and time_call.hour<=11:
        Speak(f'It is {time_call.hour} and {time_call.minute} minute AM')
    elif time_call.hour==12:
        Speak(f'It is 12 and {time_call.minute} minute PM')
    elif time_call.hour>=12:
        Speak(f'It is {time_call.hour-12} and {time_call.minute} minute PM')
    else:
        Speak(f'It is {time_call.hour} and {time_call.minute} minute Sir')

#Time in 24Hour formate-------------------------------------------------------------
# def time_Tell():
#     time_call = datetime.now()
#     tick = (datetime.now())
#     if time_call.hour>=0 and time_call.hour<12:
#         Speak(f'It is {time_call.hour} hour and {time_call.minute} minute AM')
#     else:
#         Speak(f'It is {time_call.hour} hour and {time_call.minute} minut PM')



def get_today_date():
    # Get today's date
    today_date = datetime.now().strftime("%Y-%m-%d")
    return today_date

def get_today_day():
    # Get today's day
    today_day = datetime.now().strftime("%A")
    # print(today_day)
    return today_day
    

# if  __name__ == "__main__":
#             while  True:
#                 query = Listen().lower()
#                 if "date" in query or "aaj date kya hai" in query or "What date" in query:
#                         Speak("Today's date is " + get_today_date())

#                 elif "day" in query or "aaj din kya hai " in query or "What day" in query or "today" in query:
#                     Speak("Today is " + get_today_day())

                
#                 elif 'time' in query or "time kya hua" in query:
#                     time_Tell()