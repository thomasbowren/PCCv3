def main():
    city = input("City: ")
    country = input("Country: ")
    city_country = get_city_country(city, country)
    print(f"Your chosen locale is {city_country}.")


def get_city_country(city, country, population=None):
    if population:
        population = str(population)
        locale = f"{city.title()}, {country.title()} - population {population}"
    else:
        locale = f"{city}, {country}".title()
    return locale

if __name__ == "__main__":
    main()