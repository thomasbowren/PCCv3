from pathlib import Path

def main():
    dracula_reader()
    frankenstein_reader()

def dracula_reader():
    path = Path('dracula.txt')
    contents = path.read_text(encoding = 'utf-8')
    print(f"The novel Dracula contains the words the {contents.lower().count('the ')} times.")

def frankenstein_reader():
    path = Path('frankenstein.txt')
    contents = path.read_text(encoding = 'utf-8')
    print(f"The novel Frankenstein; Or, The Modern Prometheus contains the words the {contents.lower().count('the ')} times.")


if __name__ == "__main__":
    main()