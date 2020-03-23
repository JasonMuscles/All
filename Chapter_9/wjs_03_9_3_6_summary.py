# Page-153（9-6）
# An ice cream stand is a specific kind of restaurant.Write a class called IceCreamStand that inherits from
# the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171).
# Either version of the class will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors. Create an instance ofIceCreamStand, and call this method.


# class Restaurant():
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name.title()
#         self.cuisine_type = cuisine_type.title()
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         msg = self.restaurant_name + " serves wonderful " + self.cuisine_type
#         print("\n" + msg)
#
#     def open_restaurant(self):
#         msg = self.restaurant_name + " is open. Come on in!"
#         print("\n" + msg)
#
#     def set_number_served(self, numbers):
#         self.number_served = numbers
#
#     def increment_number_served(self, numbers):
#         self.number_served += numbers
#
#
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type='ice_cream'):
#         super().__init__(restaurant_name, cuisine_type)
#
#         self.flavors = []
#
#     def show_flavors(self):
#         print("\nWe have the following flavors available:")
#         for flavor in self.flavors:
#             print("/" + flavor.title())


# ice_cream = IceCreamStand("'milk ice_cream storm'")
# ice_cream.flavors = ("milk", "milk_chocolate", "black_milk")
#
# ice_cream.describe_restaurant()
# ice_cream.show_flavors()


# Page-153（9-7）
# An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in
# Exercise 9-3 (page 166) or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list of strings
# like "can add post", "can delete post", "can ban user", and so on. WRite a method called show_privileges() that
# lists the administrator’s set of privileges. Create an instance of Admin, and call your method.


# class User():
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0
#
#     def describe_user(self):
#         msg = "User’s information " + self.first_name + " " + self.last_name
#         print(msg)
#
#     def greet_user(self):
#         greet_msg = "Hello " + self.first_name + " " + self.last_name
#         print(greet_msg)
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
# class Admin(User):
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name)
#         self.first_name = first_name
#         self.last_name = last_name
#         self.privileges = []
#
#     def show_privileges(self):
#         for privilege in self.privileges:
#             print(privilege)
#
#
# jason_privilege = Admin("Jason", "wang")
# jason_privilege.describe_user()
# jason_privilege.privileges = ["can add post", "can delete post", "can ban user"]
#
# jason_privilege.show_privileges()


# Page-153（9-8）
# Write a separate Privileges class. The class should have one attribute, privileges,
# that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class.
# Make aPrivileges instance as an attribute in the Admin class.
# Create a new instance of Admin and use your method to show its privileges.


class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        msg = "User’s information " + self.first_name + " " + self.last_name
        print(msg)


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name):
        """Initialize the admin."""
        super().__init__(first_name, last_name)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()


class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")
#
#
# jason = Admin("jason", "wang")
# jason.describe_user()
# jason.privileges.show_privileges()
#
# print("\nAdding privileges...")
# jason_privileges = [
#     "can add post",
#     "can delete post",
#     "can ban user"
# ]
#
# jason.privileges.privileges = jason_privileges
# jason.privileges.show_privileges()


# Page-153（9-8）
# Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery().
# This method should check the battery size and set the capacity to 85 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once,
# and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range.


# class Car():
#     """A simple attempt to represent a car."""
#
#     def __init__(self, manufacturer, model, year):
#         """Initialize attributes to describe a car."""
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles
#
#
# class Battery():
#     """A simple attempt to model a battery for an electric car."""
#
#     def __init__(self, battery_size=60):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         if self.battery_size == 60:
#             range = 140
#         elif self.battery_size == 85:
#             range = 185
#
#         message = "This car can go approximately " + str(range)
#         message += " miles on a full charge."
#         print(message)
#
#     def upgrade_battery(self):
#         """Upgrade the battery."""
#         if self.battery_size == 60:
#             self.battery_size = 85
#             print("Upgraded the battery to 85 kWh.")
#         else:
#             print("The battery is already upgraded.")
#
#
# class ElectricCar(Car):
#     """Models aspects of a car, specific to electric vehicles."""
#
#     def __init__(self, manufacturer, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(manufacturer, model, year)
#         self.battery = Battery()
#
#
# tesla_model = ElectricCar("Tesla", "model3", "2018")
# tesla_model.battery.get_range()
# tesla_model.battery.describe_battery()
#
# print("\nUpgrading....")
# tesla_model.battery.upgrade_battery()
# tesla_model.battery.describe_battery()







