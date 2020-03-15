# Page-104（7-1）
# Write a program that asks the user what kind of rental car they would like.
# Print a message about that car, such as “Let me see if I can find you a Subaru”.


# rental_car = input("what kind of rental car they would like?\n")
# print("Let me see if I can find you a " + rental_car.title() + ".")


# Page-104（7-2）
# Write a program that asks the user how many people are in their dinner group. If the answer is more than eight,
# print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.


# dinner_group = input("how many people are in their dinner group?\n")
# try:
#     if int(dinner_group) <= 8:
#         print("That their table is ready.")
#     else:
#         print("They’ll have to wait for a table.")
# except ValueError:
#     print("Please right number input!")


# Page-104（7-3）
# Ask the user for a number, and then report whether the number is a multiple of 10 or not.

user_number = input("Please number input!\n")
try:
    if int(user_number) % 10 == 0:
        print(user_number + " is a multiple of 10 !")
    else:
        print(user_number + " is't a multiple of 10 !")
except ValueError:
    print("Please right number input!")








