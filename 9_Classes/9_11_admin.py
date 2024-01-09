import admin

def main():
    count = input("How many new users? ")
    for _ in range(int(count)):        
        first_name = input("Provide the first name of the user: ")
        last_name = input("Provide the last name of the user: ")
        attributes = attribute_builder()
        current_user = admin.User(first_name, last_name, attributes)
        print()
        current_user.greet_user()
        current_user.describe_user()
        new_user = admin.Admin(first_name, last_name, attributes)
        new_user.privileges.show_privileges()

def attribute_builder():
    if input("Do you have additional profile attributes to add? ('Y' or 'N') ").upper() == 'Y':
        attributes = []
        while True:
            print("Enter 'q' to quit.")
            attribute = input("Attribute: ")
            if attribute == 'q' or attribute == 'Q':
                return attributes
            attributes.append(attribute)
            
if __name__ == "__main__":
    main()