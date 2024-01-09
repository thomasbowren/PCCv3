class User:
    def __init__(self, first_name, last_name, args):
        """Defines first and last name, and provides the option to specify additional arguments."""
        self.first_name = first_name
        self.last_name = last_name
        self.additional = args
        self.name = f"{self.first_name.title()} {self.last_name.title()}"
        self.login_attempts = 0
         
    def greet_user(self):
        """Greets user"""
        print(f"Hello, {self.name}")

    def describe_user(self):
        """Prints string defining user attributes."""
        print(f"User {self.name} has the following profile attributes: ")
        if self.additional:
            details = []
            details = self.additional
            for detail in self.additional:
                print(f"- {detail.title()}")

    def increment_login_attempts(self, attempt):
        if attempt > 0:
            self.login_attempts += attempt
            print("Updating login_attempt log...")
        else:
            print("Login attempts cannot be undone.")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Resetting login_attempt count...")

    def show_login_attempts(self):
        print(f"The current login_attempt count is {self.login_attempts}.")

def main():
    count = input("How many new users? ")
    for _ in range(int(count)):        
        first_name = input("Provide the first name of the user: ")
        last_name = input("Provide the last name of the user: ")
        attributes = attribute_builder()
        current_user = User(first_name, last_name, attributes)
        print()
        current_user.greet_user()
        current_user.describe_user()
        print()
        current_user.show_login_attempts()
        current_user.increment_login_attempts(5)
        current_user.show_login_attempts()
        current_user.increment_login_attempts(-5)
        current_user.show_login_attempts()
        current_user.reset_login_attempts()
        current_user.show_login_attempts()

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