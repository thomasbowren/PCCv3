def main():
    
    Person_1 = {
        'first_name' : 'tanya', 
        'last_name' : 'bowren', 
        'age' : 35, 
        'city' : 'searcy',
        }

    Person_2 =  {
        'first name' : 'everly',
        'last name' : 'bowren',
        'age' : 6,
        'city' : 'searcy',
        }

    Person_3 = {
        'first name' : 'thomas',
        'last name' : 'bowren',
        'age' : 33,
        'city' : 'searcy',
        }

    People = [Person_1, Person_2, Person_3,]


    for person in People:
       print('\n')
       for demographic, values in person.items():
          if demographic != 'age':
             print(f"\n{demographic.title()}:\t{values.title()}")
          else:
             print(f'\n{demographic.title()}:\t{values}')

    print('\n')
              
main()
       

