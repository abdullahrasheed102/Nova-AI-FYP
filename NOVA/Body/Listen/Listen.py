from googletrans import Translator
import speech_recognition as sr

#  
def Listen(language): #listeninig...
    # take microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        r.energy_threshold = 3500
        r.dynamic_energy_threshold = True
        print("\033[35m" + "Listening...")
        audio = r.listen(source, phrase_time_limit=15)
        r.pause_threshold = 0.5 #less the number, more it hears
        audio = r.listen(source,0,6) # 0,6 means cut and listen after every 6 SECONDS 
    
    try:
        print("\033[32m" + "Recognizing...")
        if language == "hin":
            query = r.recognize_google(audio, language='hi-In') #for Hindi
            query = Translate_urdu_hindi_into_eng(query)
        else:
            query = r.recognize_google(audio, language='eng-in') #for English
            print("\033[33m" + f"User: " + "\033[38m" + f"{query}")
            # print(f'Me:"{str(query)}"\n')
    except Exception as e:
        # print(e) #show full error
        print("Say that again please...")
        return "None"
    return query.lower()


def Translate_urdu_hindi_into_eng(text):
    line = str(text)
    translator = Translator()
    result = translator.translate(line)
    data = result.text
    
    print(f"ME(Urdu/Hindi->English): {data}.")
    return data
    
