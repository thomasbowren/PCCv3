def main():

    shirt_size = input("What size shirt?: ")
    message = input("What message would you like your t-shirt to display? ")

    make_shirt(shirt_size, message)
    make_shirt(message="attack on titan", size="l")

def make_shirt(size, message):
    print(f"\nWe have received your order for a size {size.title()} {message.title()} shirt.")

if __name__ == "__main__":
    main()