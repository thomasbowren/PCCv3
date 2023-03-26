def main():
    
    favorite_places = {'geralt' : ['rivia', 'khaer moran', 'skellige'], 
        'yennifer' : ['aretuza', 'vengerberg'], 
        'ciri' : ['cintra', 'khaer moran']}

    for person in favorite_places.keys():
        print(f"\n{person.title()}:")
        for place in favorite_places[person]:
            print(f"\t{place.title()}")

    print("")
    
main()
