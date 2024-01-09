def main():
    messages = ['I don\'t want to talk right now!', 'Leave me alone!', 'Sorry, cannot get to the fucking phone right now.', 'Can\'t answer, I\'m on the shitter.',]
    show_messages(messages)

def show_messages(messages):
    """Prints text messages contained witin list object."""
    for message in messages:
        print(message)

if __name__ == "__main__":
    main()