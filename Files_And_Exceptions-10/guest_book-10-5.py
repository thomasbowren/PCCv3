from pathlib import Path

def main():
    path = Path('guest_book.txt')
    names = ''
    while True:
        name = input("Enter your first and last name. Press 'q' to when all names have been entered: ")
        if name == 'q':
            break
        else:
            names += f'{name}\n'
    path.write_text(names)

if __name__ == "__main__":
    main()