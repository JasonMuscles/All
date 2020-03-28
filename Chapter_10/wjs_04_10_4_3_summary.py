# Page-185（10-11）
# Write a program that prompts for the user’s favorite number. Use json.dump() to store this number in a file.
# Write a separate program that reads in this value and prints the message, “I know your favorite number! It’s __.”


# import json
#
# favorite_number = input("Please enter your favorite number：\n")
#
# file_name = "favorite_number.json"
#
# with open(file_name, "w")as file_object:
#     json.dump(favorite_number, file_object)
#
# with open(file_name)as file_object:
#     number = json.load(file_object)
#     print("I know your favorite number! It’s " + number + ".")


# Page-185（10-12）
# Combine the two programs from Exercise 10-11 into one file. If the number is already stored, report the favorite
# number to the user. If not, prompt for the user’s favorite number and store it in a file. Run the program twice
# to see that it works.


# import json
#
#
# file_name = "favorite_number.json"
#
# try:
#     with open(file_name)as file_object:
#         number = json.load(file_object)
#         print("I know your favorite number! It’s " + number + ".")
#
# except FileNotFoundError:
#     favorite_number = input("Please enter your favorite number：\n")
#     with open(file_name, "w")as file_object:
#         json.dump(favorite_number, file_object)


# Page-185（10-13）
# The final listing for remember_me.py assumes either that the user has already entered their username or that the
# program is running for the first time. We should modify it in case the current user is not the person who last used
# the program.Before printing a welcome back message in greet_user(), ask the user if this is the correct username.
# If it’s not, call get_new_username() to get the correct username.


# import json
#
#
# def get_stored_username():
#     """Get stored username if available."""
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
#
#
# def get_new_username():
#     """Prompt for a new username."""
#     username = input("What is your name? ")
#     filename = 'username.json'
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#     return username
#
#
# def greet_user():
#     """Greet the user by name."""
#     username = get_stored_username()
#
#     if username:
#         correct = input("Are you " + username + "? (y/n) ")
#         if correct == "y":
#             print("Welcome back, " + username + "!")
#
#         else:
#             username = get_new_username()
#             print("We'll remember you when you come back, " + username + "!")
#
#     else:
#         username = get_new_username()
#         print("We'll remember you when you come back, " + username + "!")
#
#
# greet_user()
