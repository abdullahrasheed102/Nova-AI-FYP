import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATA_DIR


def load_qa_data(file_path):
    qa_dict = {}
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(":")
            if len(parts) != 2:
                continue
            q, a = parts
            qa_dict[q] = a
    return qa_dict

qa_file_path = os.path.join(DATA_DIR, "qna.txt")
try:
    qa_dict = load_qa_data(qa_file_path)
except OSError:
    qa_dict = {}
    print("Q&A data unavailable; continuing without local Q&A data.")
