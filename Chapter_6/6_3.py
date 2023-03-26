def main():
    Glossary = {
        'Boolean Expression' : 'Asks a question that evaluates to either True or False.', 
        'Logical Operator' : 'Connects Comparative Operator evaluations and includes And, Or, and !=.',
        'Comparative Operator' : 'Compares two values to determine whether the Boolean Expression evaluates to True or False.',
        'Dictionary' : 'Contains one or more Key-Value pairs.',
        'List' : 'Includes one or more Strings, Numbers, Variables, Dictionaries, or other data types within a variable.',
        }

    print(f"\nBoolean Expression:\t{Glossary['Boolean Expression']}")
    print(f"\nLogical Operator:\t{Glossary['Logical Operator']}")
    print(f"\nComparative Operator:\t{Glossary['Comparative Operator']}")
    print(f"\nDictionary:\t\t{Glossary['Dictionary']}")
    print(f"\nList:\t\t\t{Glossary['List']}")

main()