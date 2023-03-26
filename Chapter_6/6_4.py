def main():
    Glossary = {
        'Boolean Expression' : 'Asks a question that evaluates to either True or False.', 
        'Logical Operator' : 'Connects Comparative Operator evaluations and includes And, Or, and !=.',
        'Comparative Operator' : 'Compares two values to determine whether the Boolean Expression evaluates to True or False.',
        'Dictionary' : 'Contains one or more Key-Value pairs.',
        'List' : 'Includes one or more Strings, Numbers, Variables, Dictionaries, or other data types within a variable.',
        }

    for term, definition in Glossary.items():
        if term == 'Dictionary':
            print(f'\n{term}:\t\t{definition}')
        elif term == 'List':
            print(f'\n{term}:\t\t\t{definition}')
        else:
            print(f'\n{term}:\t{definition}')
      
    print('\n')

main()