def main():

    favorite_languages = {
        'jen' : 'python',
        'sarah' : 'c',
        'edward' : 'rust',
        'phil' : 'python',
    }

    friends = ['tanya', 'jen', 'everly', 'sarah', 'lumen', 'edward', 'velma', 'phil',]

    for friend in friends:
        if friend in favorite_languages.keys():
            print(f'\nThank you for taking the poll, {friend.title()}!')
        else:
            print(f'\nYou should take the poll, {friend.title()}!')

    print('\n')

main()