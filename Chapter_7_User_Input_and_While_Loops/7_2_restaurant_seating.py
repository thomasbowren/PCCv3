def main():

    party_count = int(input("How many people are in your party? "))

    if party_count > 7:
        print("\nYou'll have to wait for a table.\n")
    else:
        print("\nI guess since it's less than 8 you can come right this way, folks.")
        print("I guess sometimes it pays to be a loser!")
        print(f"You know, since you're saying your party is only {party_count} big.\n")


if __name__ == "__main__":
    main()