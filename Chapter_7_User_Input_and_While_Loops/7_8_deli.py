def main():

    sandwich_orders = ['rueben', 'club', 'meatball sub', 'pb & j', 'pastrami', 'tuna', 'pastrami', 'philly cheese steak', 'pastrami',]
    finished_sandwiches = []

    while sandwich_orders:
        sandwich = sandwich_orders.pop()
        print(f"\nI made your {sandwich.title()} Sandwich.")
        finished_sandwiches.append(sandwich)

    print('\n')

    for sandwich in finished_sandwiches:
        print(f"\nA {sandwich.title()} Sandwich has been made. Enjoy, you fat fuck!")
    
main()