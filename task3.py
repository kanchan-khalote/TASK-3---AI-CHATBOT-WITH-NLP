import nltk
from nltk.chat.util import Chat, reflections

# NLTK ke liye data download (pehli baar run karte waqt uncomment karein)
# nltk.download('punkt')

pairs = [
    [
        r"(hi|hello|hey|hii|hlo)",
        ["Hello! How can I help you?", "Hi there! Ask me anything."]
    ],
    [
        r"(what is your name|who are you)",
        ["I am a simple Chatbot made using Python and NLTK.", ]
    ],
    [
        r"(how are you|how are you doing)",
        ["I'm doing well! How can I assist you today?", ]
    ],
    [
        r"(bye|exit|quit)",
        ["Goodbye! Have a great day!", ]
    ],
    [
        r"(.*)",
        ["I am sorry, I don't understand that. Can you ask something else?", ]
    ],
]

def chatbot():
    print("Welcome! Type 'exit' to leave the chat.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
