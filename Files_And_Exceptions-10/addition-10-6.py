def main():
    """Prompts user for 2 ints to add together and demonstrates how a ValueError can be excepted, i.e. string data type."""
    print("Provide 2 integer numbers to be added together.")
    get_ints()

def get_ints():
    """Prompts user for 2 integers and adds them together if valid; excepts non-integer types."""
    try:
        int1 = int(input("First integer: "))
        int2 = int(input("Second integer: "))
        sum = int1 + int2
    except ValueError:
        print("Only integers can be added together. Try again, please.")
        return get_ints()
    else:
        print(f"The sum of the 2 integers is {sum}.")
    
if __name__ == "__main__":
    main()