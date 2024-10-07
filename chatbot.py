
# Import the required libraries
import random

# Define a dictionary to store the chatbot's responses
responses = {
    "hello": ["Hi! How can I assist you today?", "Hey! I'm here to help."],
    "hi": ["Hi! How can I assist you today?", "Hello! What's on your mind?"],
    "how are you": ["I'm good, thanks for asking!", "I'm awesome, thanks!"],
    "default": ["Sorry, I'm not sure what you mean.", "Can you please provide more context?"]
}

# Define a function to get a random response from the dictionary
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Create a chatbot function
def chatbot():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        print("Chatbot: " + get_response(user_input))

# Run the chatbot
chatbot()