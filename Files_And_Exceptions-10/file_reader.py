from pathlib import Path

def main():
    path = Path('pi_million_digits.txt')
    contents = path.read_text().rstrip()
    print(contents)

if __name__ == "__main__":
    main()