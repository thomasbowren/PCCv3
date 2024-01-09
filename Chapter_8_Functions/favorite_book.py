def main():
    book = input("What is your favorite book?\t")
    favorite_book(book)
    return 0

def favorite_book(title):
    print(f"Ah, I see your favorite book is {title.title()}.")

if __name__ == "__main__":
    main()