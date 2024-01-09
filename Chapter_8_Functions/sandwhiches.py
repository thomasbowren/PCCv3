def main():
    make_sandwhich('steak', 'mushrooms', 'onions', 'bell peppers', 'cheese whiz')
    
def make_sandwhich(*toppings):
    """Gets toppings from customer and summarizes sandwhich."""
    print(f"Your order for a sandwhich has been received with the following toppings: ")
    for topping in toppings:
        print(f" - {topping.title()}")
if __name__ == "__main__":
    main()