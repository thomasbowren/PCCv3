def main():

    prompt = "\nHow old are you?  "
    checkout_prompt = "\nDo you wish to continue? Enter 'y' for yes or 'n' for no: "
    checkout_confirm = "Enter 'confirm' to confirm your selection and checkout.\n"
    get_age = True
    print_checkout = True

    while get_age:
        age = int(input(prompt))
        if age < 4:
            print("Your ticket is free today!")
        elif age < 13:
            print("Your ticket is $10.")
        elif age > 12:
            print("Your ticket is $15.")
        
        confirm = input(checkout_prompt)
        if confirm.upper() != 'Y':            
            confirm = input(checkout_confirm)
            if confirm.upper() == 'CONFIRM':
                get_age = False

main()