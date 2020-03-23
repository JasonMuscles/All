# Page-147（9-4）
# Start with your program from Exercise 9-1 (page 166). Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class. Print the number of customers the restaurant has served,
# and then change this value and print it again.Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and print the value again.Add a method called
# increment_number_served() that lets you increment the number of customers who’ve been served. Call this method
# with any number you like that could represent how many customers were served in, say, a day of business.


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
# restaurant = Restaurant("jason restaurant", "pizza")
# restaurant.set_number_served(3)
# print("there're " + str(restaurant.number_served) + " customers that have been served.")
#
# restaurant.increment_number_served(1)
# print("there're " + str(restaurant.number_served) + " customers that have been served.")
#
# restaurant.increment_number_served(5)
# print("there're " + str(restaurant.number_served) + " customers that have been served.")


# Page-147（9-5）
# Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166).
# Write amehtod called increment_login_attempts() that increments the value of login_attempts by 1.
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times.
# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
# Print login_attempts again to make sure it was reset to 0.


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
# user = User(first_name="jason", last_name="wang")
# user.increment_login_attempts()
# print(user.login_attempts)
#
# user.increment_login_attempts()
# print(user.login_attempts)
#
# user.reset_login_attempts()
# print(user.login_attempts)








