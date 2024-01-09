from name_function import get_formatted_name

def main():
    print("Enter 'q' at any time to quit.")
    while True:
        first = input("\nPlease give me a first name: ")
        if first == 'q':
            break
        last = input("Please give me a last name: ")
        if last == 'q':
            break
        formatted_name = get_formatted_name(last, first)
        print(f"\t Neatly formatted name: {formatted_name}.")

if __name__ == "__main__":
    main()
