# Page-142（9-1）
# Make a class called Restaurant. The __init__() method for Restaurant should store two attributes:
# a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.


# class Restaurant():
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name.title()
#         self.cuisine_type = cuisine_type.title()
#
#     def describe_restaurant(self):
#         msg = self.restaurant_name + " serves wonderful " + self.cuisine_type
#         print("\n" + msg)
#
#     def open_restaurant(self):
#         msg = self.restaurant_name + " is open. Come on in!"
#         print("\n" + msg)
#
#
# restaurant = Restaurant("jason restaurant", "pizza")
# print(restaurant)
# print(restaurant.cuisine_type)
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()


# Page-142（9-2）
# Start with your class from Exercise 9-1. Create three different instances from the class,
# and call describe_restaurant() for each instance.


# class Restaurant():
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name.title()
#         self.cuisine_type = cuisine_type.title()
#
#     def describe_restaurant(self):
#         msg = self.restaurant_name + " serves wonderful " + self.cuisine_type
#         print("\n" + msg)
#
#     def open_restaurant(self):
#         msg = self.restaurant_name + " is open. Come on in!"
#         print("\n" + msg)
#
#
# fast_food = Restaurant("KFC restaurant", "Hamburg")
# fast_food.describe_restaurant()
#
# shanghai_food = Restaurant("shanghai restaurant", "won ton")
# shanghai_food.describe_restaurant()
#
# sichuan_food = Restaurant("sichuan restaurant", "hotpot")
# sichuan_food.describe_restaurant()


# Page-142（9-3）
# Make a class called User. Create two attributes called first_name and last_name,
# and then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user’s information.
# Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.


# class User():
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def describe_user(self):
#         msg = "User’s information " + self.first_name + " " + self.last_name
#         print(msg)
#
#     def greet_user(self):
#         greet_msg = "Hello " + self.first_name + " " + self.last_name
#         print(greet_msg)
#
#
# user = User(first_name="jason", last_name="wang")
# user.describe_user()
# user.greet_user()

