def main():

    prompt = "\n\nHow old are you? Enter age to continue or 'quit' to exit: "
    checkout_prompt = "\nDo you wish to continue? Enter 'y' for yes or 'n' for no: "
    checkout_confirm = "Enter 'confirm' to confirm your selection and checkout.\n"
    get_age = True
    print_checkout = True

    while get_age:
        age = input(prompt)
        if age == 'quit':
            break
        elif int(age) < 2:
            print("\nI'm sorry, you and your kind will have to leave NOW, BABY!\n")
            break
        elif int(age) < 4:
            print("\nYour ticket is free today!")
        elif int(age) < 13:
            print("\nYour ticket is $10.")
        elif int(age) > 12:
            print("\nYour ticket is $15.")
        confirm = input(checkout_prompt)
        if confirm.upper() != 'Y':            
            confirm = input(checkout_confirm)
            if confirm.upper() == 'CONFIRM':
                get_age = False
    

main()