def chatbot():
    print("Hello, I'm a simple chatbot")
    while True:
        user_input = input("You: ")
        if user_input == "hi" or user_input == "hello":
            print("Chatbot: Hello! How can I help you?")
        elif user_input == "bye":
            print("Chatbot: Bye! Have a great day.")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand ")

if __name__ == "__main__":
    chatbot()
