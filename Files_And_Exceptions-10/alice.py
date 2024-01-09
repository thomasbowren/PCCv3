from pathlib import Path

def main():
    filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
    for filename in filenames:
        path = Path(filename)
        count_words(path)
    
def count_words(path):
    """Count thge approximate number of words in a file."""
    try:
        contents = path.read_text(encoding = 'utf-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


if __name__ == "__main__":
    main()