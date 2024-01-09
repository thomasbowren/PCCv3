def main():
    shirt_size = input("Enter your shirt size: ")
    shirt_message = input("Enter the message you would like to display: ")
    make_shirt(shirt_message.title(), shirt_size.upper())

def make_shirt(message, size='L'):
    print(f"Your order of size {size} shirt with message '{message}' has been placed.")

if __name__ == "__main__":
    main()