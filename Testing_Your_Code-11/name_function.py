def main():
    first = input("First: ")
    last = input("Last: ")
    name = get_formatted_name(last, first)
    print(f"{name}")

def get_formatted_name(last, first, middle=''):
    """Gets first and last name, and returns a neatly formattted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

if __name__ == "__main__":
    main()