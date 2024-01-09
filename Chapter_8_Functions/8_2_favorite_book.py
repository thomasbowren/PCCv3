def main():

    answer = input("What is one of your favorite books?\t")

    favorite_book(answer)

def favorite_book(title):
    print(f"One of your favorite books is {title.title()}.")
          
if __name__ == "__main__":
    main()

          

              