from pathlib import Path
import json

def main():
    path = Path('favorite_number.json')
    stored_fave_number = read_favorite_number(path)
    if stored_fave_number:
        print(stored_fave_number)
    else:
        favorite_number = get_favorite_number()
        path.write_text(favorite_number)
        stored_fave_number = read_favorite_number(path)
        print(stored_fave_number)

def get_favorite_number():
    """Retrieves the favorite number of the User."""
    number = int(input("What is your favorite number? "))
    favorite_number = json.dumps(number)
    return favorite_number

def read_favorite_number(path):
    """Reads favorite number stored in json file and displays it on screen."""
    if path.exists():
        contents = path.read_text()
        if contents:
            favorite_number = json.loads(contents)
            return favorite_number
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    main()