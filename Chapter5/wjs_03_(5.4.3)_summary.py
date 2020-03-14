# Page-79（5-8）
# Make a list of five or more user names, including the name 'admin'.
# Imagine you are writing code that will print a greeting to each user after they log in to a website.
# Loop through the list, and print a greeting to each user:
# • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Eric, thank you for login in again.


# user_names = ["admin", "jason", "marry", "tom", "jerry"]
#
#
# for user in user_names:
#     if user == "admin":
#         print("Hello admin, would you like to see a status report ?")
#     else:
#         print("Hello " + user + ", thank you for login in again.")


# Page-79（5-9）
# Add an if test to hello_admin.py to make sure the list of users is not empty.
# •	If the list is emtpy, print the message We need to find some users!
# •	Remove all of the user names from your list, and make sure the correct message is printed.


# user_names = []
#
# if user_names:
#     for user in user_names:
#         if user == "admin":
#             print("Hello admin, would you like to see a status report ?")
#         else:
#             print("Hello " + user + ", thank you for login in again.")
# else:
#     print("We need to find some users!")


# Page-79（5-10）
# Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# •	Make a list of five or more user names called current_users. Make another list of five user names called new_users.
# Make sure one or two of the new user names are also in the current_users list.
# •	Loop through the new_users list to see if each new username has already been used. If it has,
# print a message that the person will need to enter a new username. If a username has not been used,
# print a message saying that the username is available.
# •	Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.


# current_users = ["jason", "jerry", "tom", "marry", "harry", "jeff"]
# new_users = ["jason", "Jerry", "rose", "mark", "summer"]
#
# current_users_lower = [user.lower() for user in current_users]
#
# for new_user in new_users:
#     if new_user.lower() in current_users_lower:
#         print("The name has be used! change an other name")
#     else:
#         print("the username is available")


# Page-80（5-11）
# Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end inth,
# except 1, 2, and 3.
# •	Store the numbers 1 through 9 in a list.
# •	Loop through the list.
# •	Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
# Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
numbers_list = list(range(1, 10))
print(numbers_list)

for number in numbers_list:

    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")









