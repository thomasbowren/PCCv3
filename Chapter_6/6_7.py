def main():
    
    Person_1 = {
        'first_name' : 'tanya', 
        'last_name' : 'bowren', 
        'age' : 35, 
        'city' : 'searcy',
        }

    Person_2 =  {
        'first_name' : 'everly',
        'last_name' : 'bowren',
        'age' : 6,
        'city' : 'searcy',
        }

    Person_3 = {
        'first_name' : 'thomas',
        'last_name' : 'bowren',
        'age' : 33,
        'city' : 'searcy',
        }

    People = [Person_1, Person_2, Person_3,]


    for person in People:
       print('\n')
       for demographic in person.values():
          print(f"{demographic}")
              
       

    print('\n')

main()