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


print("Enter:'quit' when you are finished!")

while True:
    try:
        num_a = int(input("please input number a : "))
        if num_a == "quit":
            break

        num_b = int(input("please input number b : "))
        if num_b == "quit":
            break

    except ValueError:
        print("please input right number! ")

    else:
        count = num_a + num_b
        print(str(num_a) + " + " + str(num_b) + " = " + str(count))







