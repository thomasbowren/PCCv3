from random import randint

def main():
    if input("Would you like to select custom dice? (Enter 'Y' or 'N'): ").upper() == 'Y':
        dice(get_sides())
    else:
        dice()

def dice(sides=6):
    print(f"You rolled a {randint(1, sides)}.")

def get_sides():
    return int(input("Choose your die by stating the number of sides needed: "))

if __name__ == "__main__":
    main()

    