def main():

    prompt = f"\nChoose which topping to add to your pizza next."
    prompt += " Press 'quit' to confirm your toppings"
    
    topping_update = True

    while topping_update:
        topping = input(prompt + ": ")
        if topping == 'quit':
            topping_update = False
        if topping != 'quit':
            print(f"\n{topping.title()} has been added to your pie!")
main()