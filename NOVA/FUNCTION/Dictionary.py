import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nltk.corpus import wordnet
from Body.Speak.Speak import Speak

def get_word_info(word):
    meanings = []
    synonyms = []

    # Get meanings and synonyms for the word
    for synset in wordnet.synsets(word):
        # Split definition into words and take the first three words
        meaning_words = synset.definition().split()
        # Join the first three words to form the meaning
        meaning = ' '.join(meaning_words)
        meanings.append(meaning)
        
        synonyms.extend(synonym.replace('_', ' ') for synonym in synset.lemma_names())

    # Remove duplicates from synonyms and limit to top 3
    synonyms = list(set(synonyms))[:3]

    return meanings[:3], synonyms


def Dict_Meanings(word):
    meanings = get_word_info(word)[0]

    if meanings:
        print(f"Meanings of '{word}':")
        for i, meaning in enumerate(meanings, start=1):
            Speak(f"{i}: {meaning}")

    else:
        Speak("I'm sorry, I couldn't find any meanings of that word.")

def Dict_Synonyms(word):
    synonyms = get_word_info(word)[1]

    if synonyms:
        print(f"Synonyms of '{word}':")
        for i, synonym in enumerate(synonyms, start=1):
            Speak(f"Synonym {i}: {synonym}")

    else:
        Speak("I'm sorry, I couldn't find any synonyms of that word.")
