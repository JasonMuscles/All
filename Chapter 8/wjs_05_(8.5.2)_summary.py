# Page-132（8-12）
# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function call provides,
# and it should print a summary of the sandwich that is being ordered. Call the function three times,
# using a different number of arguments each time.


# def make_sandwich(*items):
#     print("\nI'll make you a great sandwich:")
#     for item in items:
#         print("  ...adding " + item + " to your sandwich.")
#     print("Your sandwich is ready!")
#
#
# make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
# make_sandwich('turkey', 'apple slices', 'honey mustard')
# make_sandwich('peanut butter', 'strawberry jam')


# Page-132（8-14）
# Write a function that stores information about a car in a dictionary.
# the function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.
# Call the function with the required information and two other name-value pairs,
# such as a color or an optional feature. Your function should work for a call like this one:


def make_car(manufacturer, model, **options):
    car_dict = {
        "manufacturer": manufacturer.title(),
        "model": model.title()
    }

    for option, value in options.items():
        car_dict[option] = value

    return car_dict


my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_accord = make_car('honda', 'accord', year=1991, color='white', headlights='popup')
print(my_accord)




