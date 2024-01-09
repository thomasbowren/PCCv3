class Empoloyee:
    def __init__(self, first_name, last_name, salary):
        """Initializes Employee class and sets values for first_name, last_name, and salary attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, salary_increase=5000):
        """Increases salary attribute by amount specified by raise argument."""
        self.salary += salary_increase
    
    def show_employee_info(self):
        """Displays attributes related to employee on the screen."""
        print(f"Employee: {self.first_name} {self.last_name}.\nSalary: {self.salary}")
    
def main():
    employee = Empoloyee('Thomas', 'Bowren', 75000)
    employee.show_empoloyee_info()
    employee.give_raise()
    employee.show_employee_info()
    
if __name__ == "__main__":
    main()
    