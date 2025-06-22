import json
import random
import nltk
from nltk.stem import PorterStemmer

# Initialize stemmer
stemmer = PorterStemmer()

# Load the intents file
with open("intents.json") as file:
    data = json.load(file)

# Preprocess with simple NLP (lowercase, stem)
def preprocess(text):
    words = text.lower().split()
    return [stemmer.stem(word) for word in words]

# Match input to intent
def get_intent(user_input):
    user_words = preprocess(user_input)
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern_words = preprocess(pattern)
            if set(pattern_words).intersection(user_words):
                return intent
    return None

# Chat loop
def chat():
    print("ChatBot: Hello! Ask me Python questions. Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("ChatBot: Goodbye!")
            break
        intent = get_intent(user_input)
        if intent:
            print("ChatBot:", random.choice(intent["responses"]))
        else:
            print("ChatBot: I’m not sure about that. Try something else.")

if __name__ == "__main__":
    chat()
