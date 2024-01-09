from pathlib import Path

def main():
    path = Path('guest.txt')
    name = input("What is your name? ")
    path.write_text(f"Hello, {name}")

if __name__ == "__main__":
    main()