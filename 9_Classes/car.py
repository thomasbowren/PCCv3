class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self. model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, mileage):
        """Adds value to current mileage"""
        if mileage >= 0:
            self.odometer_reading += mileage
        else:
            print("You cannot roll back an odometer!")

class ElectricCar(Car):
    """Establishes an electric car child of the car class."""
    def __init__(self, make, model, year):
        """Initializes make, model, and year attributes for the car, as well as others specific to electric cars only. """
        super().__init__(make, model, year)
        self.battery_size = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size} - kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Analyzes current battery_size and upgrades it to a 65 kWh if it isn't already."""
        if self.battery_size < 65:
            self.battery_size = 65
            print("Your battery has been upgraded to 65 kWh.")
        elif self.battery_size == 65:
            print("Your car is not eligible for a battery upgrade given its current capacity of 65 kWh.")

def main():
    my_new_car = Car('audi', 'a4', 2024)
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()
    my_new_car.update_odometer(23_500)
    my_new_car.read_odometer()
    my_new_car.increment_odometer(-50)
    my_new_car.read_odometer()
    print()
    my_electric_car = ElectricCar('tesla', 'model 3', '2024')
    print(my_electric_car.get_descriptive_name())
    my_electric_car.battery_size.describe_battery()
    my_electric_car.battery_size.get_range()
    my_electric_car.battery_size.upgrade_battery()
    my_electric_car.battery_size.get_range()
    print()
    my_fast_electric_car = ElectricCar('tesla', 'model y', 2024)
    print(my_fast_electric_car.get_descriptive_name())
    my_fast_electric_car.battery_size.battery_size = 65
    my_fast_electric_car.battery_size.get_range()
    my_fast_electric_car.battery_size.upgrade_battery()

if __name__ == "__main__":
    main()