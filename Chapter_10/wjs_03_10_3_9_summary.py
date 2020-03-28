# Page-179（10-6）
# One common problem when prompting for numerical input occurs when people provide text instead of numbers.
# When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers.
# Add them together and print the result. Catch theTypeError if either input value is not a number,
# and print a friendly error message. Test your program by entering two numbers and then by entering some text
# instead of a number.ValueError


# while True:
#     num_a = input("please give number a: ")
#
#     if num_a == "quit":
#         break
#     num_b = input("please give number b: ")
#     try:
#         count = int(num_a) + int(num_b)
#
#     except ValueError:
#         print("please get number!")
#
#     else:
#         print(num_a + " + " + num_b + " = " + str(count))


# Page-179（10-7）
# Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers even
# if they make a mistake and enter text instead of a number.


# print("Enter:'quit' when you are finished!")
#
# while True:
#     try:
#         num_a = input("please input number a : ")
#         if num_a == "quit":
#             break
#
#         num_a = int(num_a)
#
#         num_b = input("please input number b : ")
#         if num_b == "quit":
#             break
#
#         num_b = int(num_b)
#
#     except ValueError:
#         print("please input right number! ")
#
#     else:
#         count = num_a + num_b
#         print(str(num_a) + " + " + str(num_b) + " = " + str(count))


# Page-179（10-8）
# Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs
# in the second file. Write a program that tries to read these files and print the contents of the file to the screen.
# Wrap your code ina try-except block to catch the File Not Found error, and print a friendly message if a file is
# missing.Move one of the files to a different location on your system, and make sure the code in the except block
# executes properly.


# files_name = ["cats.txt", "dogs.txt"]
#
#
# def files(file_name):
#
#     try:
#         with open(file_name) as file_object:
#             lines = file_object.readlines()
#
#     except FileNotFoundError:
#         msg = "Sorry! '" + file_name + "' does not exist."
#         print(msg)
#
#     else:
#         for line in lines:
#             print(line.rstrip())
#
#
# for f in files_name:
#     files(f)
# ===============================================================================================

# file_names = ["cats.txt", "dogs.txt"]
#
# for file_name in file_names:
#     print("Read file : " + file_name)
#     try:
#         with open(file_name) as file_object:
#             contents = file_object.read()
#
#     except FileNotFoundError:
#         msg = "Sorry! '" + file_name + "' does not exist.\n"
#         print(msg)
#
#     else:
#         print(contents + "\n")


# Page-180（10-8）
# Modify your except block in Exercise 10-8 to fail silently if either file is missing.


file_names = ["cats.txt", "dogs.txt"]

for file_name in file_names:
    print("Read file : " + file_name)
    try:
        with open(file_name) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
        pass

    else:
        print(contents + "\n")





