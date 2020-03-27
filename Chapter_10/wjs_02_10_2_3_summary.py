# Page-172（10-3）
# Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.


# file_path = "User_names.txt"
# user_name = input("input you'er name:\n")
#
# with open(file_path, "w") as file_object:
#
#     input_lines = file_object.write(user_name)
#
#
# with open(file_path) as file_object_reade:
#     reade_lines = file_object_reade.readlines()
#     for lines in reade_lines:
#         print(lines.rstrip())


# Page-172（10-4）
# Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen
# and add a line recording their visit in a file called guest_book.txt. Make sure each entry appears on a new
# line in the file.


# file_path = "guest_book.txt"
#
# print("Enter:'quit' when you are finished.")
#
# while True:
#     user_name = input("input you're name:\n")
#     if user_name == "quit":
#         break
#
#     else:
#         with open(file_path, "a") as file_object:
#             file_object.write(user_name + "\n")
#             print(user_name + " you've been added to the guest book.")


# Page-172（10-5）
# Write a while loop that asks people why they like programming. Each time someone enters a reason,
# add their reason to a file that stores all the responses.


# file_path = "reason.txt"
# print("Enter:'quit'when you are finished!")
#
# while True:
#     reason = input("why are you like programming?\n")
#     if reason == "quit":
#         break
#     else:
#         with open(file_path, "a") as file_object:
#             file_object.write(reason + "\n")


# Page-172（10-6）
# One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you
# try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers.
# Add them together and print the result. Catch theTypeError if either input value is not a number,
# and print a friendly error message.
# Test your program by entering two numbers and then by entering some text instead of a number.













