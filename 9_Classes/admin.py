import user

class Admin(user.User):
    def __init__(self, first_name, last_name, args):
        """Creates Administrator child class and initializes first_name, last_name, and args list attributes."""
        super().__init__(first_name, last_name, args)
        self.privileges = Privileges.get()

class Privileges:
    """Creates a class for privileges for use as an attribute for the Admin class."""

    def __init__(self, privileges=[]):
        """Initializes Privileges child class."""
        self.privileges = privileges
   
    @classmethod
    def get(cls):
        print("Set privileges for Admin User. Enter 'q' to quit.")
        privilege_list = []
        while True:
            privilege = input("Privilege: ")
            if privilege.lower() == 'q':
                print()
                return cls(privilege_list)
            else:
                privilege_list.append(privilege)

    def show_privileges(self):
        """Displays privileges available to Admin accounts"""
        print("Administrators have the following privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")
        print()

def main():
    count = input("How many new users? ")
    for _ in range(int(count)):        
        first_name = input("Provide the first name of the user: ")
        last_name = input("Provide the last name of the user: ")
        attributes = attribute_builder()
        current_user = user.User(first_name, last_name, attributes)
        print()
        current_user.greet_user()
        current_user.describe_user()
        new_user = Admin(first_name, last_name, attributes)
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