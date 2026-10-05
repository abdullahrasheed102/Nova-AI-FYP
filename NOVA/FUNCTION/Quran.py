import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import QURAN_DIR
from FUNCTION.platform_utils import open_path
from Body.Listen.ListenJs import Listen
from Body.Speak.Speak import Speak


def play_surah(query):
    dir_path = QURAN_DIR
    surah_number = extract_surah_number(query)
    if surah_number:
        file_name = f"{surah_number}."
        file_found = False
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.startswith(file_name) and file.endswith('.mp3'):
                    file_path = os.path.join(root, file)
                    open_path(file_path)
                    Speak("Playing Surah of Holy Quran for you...")
                    file_found = True
                    break
            if file_found:
                break
        if not file_found:
            print("File not found!")
    else:
        print("Invalid command! Please specify a valid Surah number.")

def extract_surah_number(query):
    keywords = ["start surah", "play surah", "surah", "surah number", "surat"]
    for keyword in keywords:
        if keyword in query:
            surah_name = query.replace(keyword, "").strip()
            if surah_name.isdigit():
                return surah_name
            else:
                return None
    return None


# if __name__ == "__main__":
#     while  True:
#         query = Listen().lower()
#         if any(keyword in query for keyword in ["start surah", "play surah", "surah", "surah number", "surat"]):
#             play_surah(query)




