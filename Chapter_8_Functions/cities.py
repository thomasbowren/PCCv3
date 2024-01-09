def main():
    city = input("Enter name of city: ")
    country = input("Enter name of country: ")
    if country:
        describe_city(city, country)
    else:
        describe_city(city)

def describe_city(city, country = 'United States'):
    print(f"{city.title()} is in {country.title()}.")

if __name__ == "__main__":
    main()
