def main():
    
    Heroes = {'geralt' : {
        'favorite_places' : ['rivia', 'khaer moran', 'skellige'],
        'favorite_attack' : ['silver sword',]},
        'yennifer' : {
        'favorite_places' : ['aretuza', 'vengerberg'],
        'favorite_attack' : ['sorcery'],}, 
        'ciri' :  {
        'favorite_places' : ['cintra', 'khaer moran'],
        'favorite_attack' : ['elder magick']},}

    
    for hero, bio in Heroes.items():
        print("\n")
        for _ in range(100):
            print("*", end = '')
        print("\n")
        print(f"{hero.title()}")
        for _ in range(15):
            print("_", end = '')
        count = 0
        for fact, details in bio.items():
            print("\n")
            print(f"{fact.title()}:\t", end = '')
            for detail in details:
                count += 1
                if count < len(details):
                    print(f"{detail.title()}, ", end = '')
                else:
                    print(f"{detail.title()}.", end = '')

    print("")
    
main()
        