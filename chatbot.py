import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "How can I help you today?"]
    ],
    [
        r"how are you ?",
        ["I'm good, thank you!", "I'm doing well. How can I assist you?"]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Take care!"]
    ],
]

def chatbot():
    print("Hello! I'm your chatbot. Type 'exit' to end the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download('punkt')
    chatbot()
