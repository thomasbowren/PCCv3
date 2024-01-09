from pathlib import Path
import json

def main():
    path = Path('favorite_number.json')
    favorite_number = read_favorite_number(path)
    print(favorite_number)

def read_favorite_number(path):
    """Reads favorite number stored in json filed and displays it on screen."""
    contents = path.read_text()
    favorite_number = json.loads(contents)
    return favorite_number

if __name__ == "__main__":
    main()