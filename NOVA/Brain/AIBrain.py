import os
import sys 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATA_DIR

# API credentials are loaded locally and are never printed.
try:
    with open(os.path.join(DATA_DIR, "API.txt"), encoding="utf-8") as fileopen:
        API = fileopen.read().strip()
except OSError:
    API = ""
    print("API data unavailable; API-backed Brain features are disabled.")

#importing
import openai
from dotenv import load_dotenv


#coding
openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplayBrain(question, chat_log= None):
    if not API:
        return "API-backed Brain features are unavailable."
    with open(os.path.join(DATA_DIR, "API.txt"), encoding="utf-8") as FileLog:
        chat_log_template = FileLog.read()

    if chat_log is None:
        chat_log = chat_log_template
    
    prompt = f'{chat_log}You: {question} \nBuddy: '
    response = completion.create(
        model="code-davinci-002",
        prompt = prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    answer = response.choices[0].test.strip()
    chat_log_template_update = chat_log_template + f"\nYou: {question} \n Buddy: {answer}"
    log_dir = os.path.join(DATA_DIR, "DataBase")
    os.makedirs(log_dir, exist_ok=True)
    with open(os.path.join(log_dir, "chat_log.txt"), "w", encoding="utf-8") as FileLog:
        FileLog.write(chat_log_template_update)
    return answer



