from pathlib import Path

def main():
    """Reads text from dogs.txt and cats.txt, and excepts any invalid/missing files without interrupting program."""
    get_dogs()
    print()
    get_cats()

def get_dogs():
    """Attempts to read and print dogs.txt file, and handles FileNotFoundError as an exception."""
    path = Path('dogs.txt')
    try:
        dogs = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, {path} is missing.")
    else:
        for dog in dogs.splitlines():
            print(f"{dog}")
    
def get_cats():
    """Attempts to read and print cats.txt files, and handles FileNotFoundError as an exception."""
    path = Path('cats.txt')
    try:
        cats = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, {path} is missing.")
    else:
        for cat in cats.splitlines():
            print(f"{cat}")

if __name__ == "__main__":
    main()