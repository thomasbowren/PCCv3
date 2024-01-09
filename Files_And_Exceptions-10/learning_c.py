from pathlib import Path

def main():
    path = Path('learning_python.txt')
    learning_python = path.read_text()
    learning_python_lines = learning_python.splitlines()
    python_lines = ''
    print(learning_python)
    for line in learning_python_lines:
        python_lines += f" {line.replace('Python', 'C')}"
    print(python_lines)
    print(len(python_lines))

if __name__ == "__main__":
    main()