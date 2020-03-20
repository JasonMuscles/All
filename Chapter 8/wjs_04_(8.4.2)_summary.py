# Page-129（8-9）
# Make a list of magician’s names. Pass the list to a function called show_magicians(),
# with prints the name of each magician in the list.


# magician_name_list = ["Jason", "Tom", "Harry"]
#
#
# def show_magicians(magicians):
#     return print("magician's name:" + str(magicians))
#
#
# show_magicians(magician_name_list)

# ========================================================================================

# def show_magicians(magicians):
#     for magician in magicians:
#         print(magician.title())
#
#
# magicians_name_list = ["JASON", "tom", "Marry", "HArry"]
#
# show_magicians(magicians_name_list)


# Page-129（8-10）
# Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding the phrase
# the Great to each magician’s name. Call show_magicians() to see that the list has actually been modified.


# def show_magicians(magicians):
#     for magician in magicians:
#         print(magician)
#
#
# def make_great(magicians):
#
#     great_magicians = []
#
#     while magicians:
#         magician = magicians.pop()
#         great_magician = magician + " the Great"
#         great_magicians.append(great_magician)
#
#     for great_magician in great_magicians:
#         magicians_list.append(great_magician)
#
#
# magicians_list = ["JASON", "tom", "Marry", "HArry"]
# show_magicians(magicians_list)
# print("-------")
#
# make_great(magicians_list)
# show_magicians(magicians_list)


# Page-129（8-11）
# Start with your work from Exercise 8-10.
# Call the function make_great() with a copy of the list of magicians’ names.
# Because the original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original names and one list with
# the Great added to each magician’s name.


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians_list):

    great_magicians = []

    while magicians_list:
        magician = magicians_list.pop()
        great_magician = magician + " the Great"
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians_list.append(great_magician)

    return magicians_list


magicians_list = ["JASON", "tom", "Marry", "HArry"]
show_magicians(magicians_list)
print("-------")

make_greats = make_great(magicians_list[:])
show_magicians(make_greats)
print("-------")

show_magicians(magicians_list)











