def main():
   
    Rivers = {'st. lawrence' : 'canada', 'danube' : 'poland', 'thames' : 'england',}

    for river, country in Rivers.items():
        print(f'\nThe {river.title()} river runs through {country.title()}.')
        
    print('\n')

    for river in Rivers.keys():
        print(f"\n{river.title()}")
    print('\n')

    for country in Rivers.values():
        print(f'\n{country.title()}')
    print('\n')


main() 