def main():
    city_count = input("How many cities would you like to enter: ")
    city_getter(city_count)

def city_country(city, country):
    return f"{city.title()}, {country.title()}"

def city_getter(iterations):
    for _ in range(int(iterations)):
        city = input("City: ")
        country = input("Country: ")
        location = city_country(city, country)
        print(location)

if __name__ == "__main__":
    main()