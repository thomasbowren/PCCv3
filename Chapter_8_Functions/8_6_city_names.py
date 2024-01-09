def main():

    city = city_init('paris', 'france')
    print(city.title())
    print()

    city = city_init('new york', 'new york')
    print(city.title())
    print()

    city = city_init('Johanesburg', 'south africa')
    print(city.title())
    print()

def city_init(city, country):
    return f"{city}, {country}"

if __name__ == "__main__":
    main() 

