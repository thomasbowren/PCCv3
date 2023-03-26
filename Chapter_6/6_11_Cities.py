def main():

    Cities = {'New York' : {
        'Country' : 'United States',
        'Population' : '8.468 million', 
        'Fact' : 'Part of colony of New Netherland founded in 1624 where it grew into a city known as New Amsterdam.' },
        'London' : {
        'Country' : 'UK',
        'Population' : '8.982 million',
        'Fact' : 'Founded in 47 A.D. by the Romans who called it Londinium.'}, 
        'Shanghai' : {
        'Country' : 'China',
        'Population' : '26.32 million',
        'Fact' : 'First became a city in 1291; location of Chinese Communisty Party founding in 1921.'
        }}
    
    for city, stat in Cities.items():
        print("\n")
        if city == 'London':
            print(f"{city.title()}\t\t", end = "")
        else:
            print(f"{city.title()}\t", end = "")
        for _ in range(100):
            print("_", end = "")
        print("\n")
        for values in stat.keys():
            if values == 'Fact':
                tab = '\t'
            else:
                tab = ''
            print(f"{values}: \t{tab}", end = "")
            print(f"{stat[values]}")



main()