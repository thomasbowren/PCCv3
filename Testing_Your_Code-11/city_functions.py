def main():
    city = input("City: ")
    country = input("Country: ")
    city_country = get_city_country(city, country)
    print(f"Your chosen locale is {city_country}.")


def get_city_country(city, country):
    locale = f"{city}, {country}"
    return locale.title()

if __name__ == "__main__":
    main()