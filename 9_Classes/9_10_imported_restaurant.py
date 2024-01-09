from restaurant import Restaurant

class IceCreamStand(Restaurant):
  """Represents attributes of the Restaurant Class adapted to an ice cream stand."""
  def __init__(self, restaurant_name, cuisine_type):
    """Receives attrigutes chosen from the Parent Class and initializes them."""
    super().__init__(restaurant_name, cuisine_type)
    self.flavors = ['chocolate', 'strawberry', 'peach', 'raspberry', 'peanut butter']
    self.selection = []
    self.max_scoops = 3
    
  def display_flavors(self):
      """Shows ice cream flavors contained within Flavors List"""
      print(f"Choose up to {self.max_scoops} scoops from the following flavors:")
      for flavor in self.flavors:
        print(f"- {flavor.title()}")
  
  def scoop_count(self):
     """Keeps track of how many scoops customer has chosen."""
     return self.max_scoops

  def flavor_selector(self):
     """Gathers flavors from customer and compiles them in a list"""
     for _ in range(int(self.max_scoops)):
        selected = input(f"{self.display_flavors()}\n> ")
        if selected.lower() in self.flavors:
          self.selection.append(selected)
          self.max_scoops -= 1
        else:
           print("Not a valid flavor. Please, try again.\n")
           return self.flavor_selector()
        if  self.max_scoops > 0:
          if input("Would you like to add another flavor? Enter Y or N: ").title() == 'N':
            break
           
  def build_cone(self):
     """Simulates building an ice cream cone based upon the flavors added to Selection via flavor_selector()"""
     print("Excellent choice! Your order has been placed for a cone with the following flavors: ")
     for selected in self.selection:
        print(f"- {selected.title()}")

def main():
    number = input("How many restaurants are you listing in this session? ")
    for _ in range(int(number)):
      my_ice_cream_stand = IceCreamStand.get()
      print()
      my_ice_cream_stand.describe_restaurant()
      my_ice_cream_stand.flavor_selector()
      my_ice_cream_stand.build_cone()
      my_ice_cream_stand.set_number_served(_)
      my_ice_cream_stand.increment_number_served(1)
      my_ice_cream_stand.show_number_served()

if __name__ == "__main__":
   main()