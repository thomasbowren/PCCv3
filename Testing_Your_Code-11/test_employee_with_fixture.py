import pytest
from employee import Employee 

def main():
    test_employee_raise()
    test_employee_custom_raise()

@pytest.fixture
def employee():
    """Initializes an Employee object for use in testing the class."""
    employee = Employee('thomas', 'bowren', 75000)
    return employee

def test_employee_raise(employee):
    """Does the default raise of 5000 update the employee's salary?"""
    employee.give_raise()
    assert employee.salary == 80000

def test_employee_custom_raise(employee):
    """Does a custom increase of 25,000 update the employee's salary?"""
    employee.give_raise(25000)
    assert employee.salary == 100000

if __name__ == "__main__":
    main()



