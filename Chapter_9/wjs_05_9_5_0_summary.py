# Page-160（9-13）
# Start with Exercise 6-4 (page 108), where you used a standard dictionary to represent a ordered_dict.
# Rewrite the program using the OrderedDict class and make sure the order of the output matches the order in
# which key-value pairs were added to the dictionary.


# from _collections import OrderedDict
# ordered_dict = OrderedDict()
#
# ordered_dict['string'] = 'A series of characters.'
# ordered_dict['comment'] = 'A note in a program that the Python interpreter ignores.'
# ordered_dict['list'] = 'A collection of items in a particular order.'
# ordered_dict['loop'] = 'Work through a collection of items, one at a time.'
# ordered_dict['dictionary'] = "A collection of key-value pairs."
# ordered_dict['key'] = 'The first item in a key-value pair in a dictionary.'
# ordered_dict['value'] = 'An item associated with a key in a dictionary.'
# ordered_dict['conditional test'] = 'A comparison between two values.'
# ordered_dict['float'] = 'A numerical value with a decimal component.'
# ordered_dict['boolean expression'] = 'An expression that evaluates to True or False.'
#
# for ordered, definition in ordered_dict.items():
#     print(ordered.title() + ": " + definition)
#
# for key, value in ordered_dict.items():
#     print(key + ": " + value)


# Page-160（9-14）
# The module random contains functions that generate random numbers in a variety of ways. The function randint()
# returns an integer in the range you provide. the following code returns a number between 1 and 6:from random import
# randint x = randint(1, 6) Make a class Die with one attribute called sides, which has a default value of 6.
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
# Make a 6-sided die and roll it 10 times.


from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


sides_6 = Die(6)

sides_6_list = []
for result in range(10):
    sides_list = sides_6.roll_die()
    sides_6_list.append(sides_list)
print(sides_6_list)


sides_10 = Die(10)

sides_10_list = []
for result in range(10):
    sides_list = sides_10.roll_die()
    sides_10_list.append(sides_list)
print(sides_10_list)


sides_20 = Die(20)

sides_20_list = []
for result in range(10):
    sides_list = sides_20.roll_die()
    sides_20_list.append(sides_list)
print(sides_20_list)
























