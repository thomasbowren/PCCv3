def main():
    messages = ['I don\'t want to talk right now!', 'Leave me alone!', 'Sorry, cannot get to the fucking phone right now.', 'Can\'t answer, I\'m on the shitter.',]
    delivered = []
    sent_messages(messages [:], delivered)
    print(messages)

def show_messages(messages):
    """Prints text messages contained witin list object."""
    for message in messages:
        print(message)

def sent_messages(texts, delivered):
    """Simulates sending text, then creates and prints a list of sent text."""
    print("Sending Messages: ")
    while texts:
        current_text = texts.pop()
        delivered.append(current_text)
        print(current_text)
    print("\nMessages Delivered: ")
    for text in delivered:
        print(text)
        

if __name__ == "__main__":
    main()