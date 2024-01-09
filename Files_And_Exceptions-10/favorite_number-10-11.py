from pathlib import Path
import json

def main():
    path = Path('favorite_number.json')
    favorite_number = get_favorite_number()
    path.write_text(favorite_number)

def get_favorite_number():
    """Retrieves the favorite number of the User."""
    number = int(input("What is your favorite number? "))
    favorite_number = json.dumps(number)
    return favorite_number

if __name__ == "__main__":
    main()