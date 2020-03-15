# Page-113（7-8）
# Make a list called sandwich_orders and fill it with the names of various sandwiches.
# Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.
# As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made,
# print a message listing each sandwich that was made.


# sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
# finished_sandwiches = []
#
# while sandwich_orders:
#     current_sandwiches = sandwich_orders.pop()
#
#     print("I made your " + current_sandwiches + " sandwich.")
#
#     finished_sandwiches.append(current_sandwiches)
#
# for finished_sandwich in finished_sandwiches:
#     print("finished_sandwich: " + finished_sandwich)


# Page-113（7-9）
# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the
# list at least three times. Add code near the beginning of your program to print a message saying
# the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami'
# from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.


# sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef', 'pastrami', 'pastrami', 'pastrami']
# finished_sandwiches = []
#
# print("we're all out of pastrami today.")
#
# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")
#
# print("\n")
#
# current_orders = sandwich_orders
# for current in current_orders:
#     print(current)


# Page-113（7-10）
# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.


name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "
user_request = {}

while True:
    name = input(name_prompt)
    place = input(place_prompt)

    user_request[name] = place

    repeat = input(continue_prompt)
    if repeat != "yes":
        break


for name, place in user_request.items():
    print(name + " like go to " + place)


















