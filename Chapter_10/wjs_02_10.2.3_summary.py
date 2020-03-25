# Page-172（10-3）
# Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.


file_path = "User_names.txt"
user_name = input("input you'er name:\n")

with open(file_path, "w") as file_object:

    input_lines = file_object.write(user_name)


with open(file_path) as file_object_reade:
    reade_lines = file_object_reade.readlines()
    for lines in reade_lines:
        print(lines.rstrip())


# Page-172（10-4）
# Write a while loop that prompts users for their name. When they enter their name,
# print a greeting to the screen and add a line recording their visit in a file called guest_book.txt.
# Make sure each entry appears on a new line in the file.





