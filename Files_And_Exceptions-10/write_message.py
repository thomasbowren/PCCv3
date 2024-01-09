from pathlib import Path

def main():
    contents = "I love programming.\n"
    contents += "I love creating new games.\n"
    contents += "I also love working with data.\n"
    path = Path('programming.txt')
    path.write_text(contents)

if __name__ == "__main__":
    main()