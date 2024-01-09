def main():

    sandwich_orders = ['rueben', 'club', 'meatball sub', 'pb & j', 'pastrami', 'tuna', 'pastrami', 'philly cheese steak', 'pastrami',]
    finished_sandwiches = []

    print("\nSorry, we're out of Pastrami you dumb bitch!")

    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    while sandwich_orders:
        sandwich = sandwich_orders.pop()
        print(f"\nI made your {sandwich.title()} Sandwich.")
        finished_sandwiches.append(sandwich)

    print('\n')

    for sandwich in finished_sandwiches:
        print(f"\nA {sandwich.title()} Sandwich has been made. Enjoy, you fat fuck!")

    print('')
    
main()