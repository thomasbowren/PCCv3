def main():

    make_shirt()

    shirt_size = input("\nWhat size shirt: ")
    make_shirt(shirt_size)

    text = input("\nWhat message would you like your shirt to display?: ")
    make_shirt(message='cyberpunk 2077', size='small')

def make_shirt(size="large", message="i love python"):
    print(f"\nWe have received your order for a size {size.title()} {message.title()} shirt.")

if __name__ == "__main__":
    main()

