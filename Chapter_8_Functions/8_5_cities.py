def main():

    city('tokyo')
    print()
    city('kyoto')
    print()
    city('shanghai', country='china')
    print()

def city(city, country='japan'):
    print(f"\n{city.title()} is in {country.title()}.")

if __name__ == "__main__":
    main()
    