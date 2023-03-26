def main():

    multiple_of_10 = int(input("\nPick a number: "))
    print("\nNow let's check whether or not it is a multiple of 10.\n")

    if multiple_of_10 % 10 == 0:
        print(f"It appears your number of {multiple_of_10} is indeed a multiple of 10.\n")
    else:
        print(f"No, your selection of {multiple_of_10} actually doesn't calculate to be a multiple of 10.\n")

if __name__ == "__main__":
    main()
