# Page-99（6-7）
# Start with the program you wrote for Exercise 6-1 (page 102). Make two new dictionaries representing different people,
# and store all three dictionaries in a list called people. Loop through your list of people.
# As you loop through the list, print everything you know about each person.


# make an empty list to store people in it
# people = []

# make two people dictionaries
# person_dic_1 = {"first name": "jason",
#                 "last name": "wang",
#                 "age": "31",
#                 "city": "CD"}
#
# person_dic_2 = {"first name": "jeff",
#                 "last name": "li",
#                 "age": "29",
#                 "city": "SH"}
#
#
# people.append(person_dic_1)
# people.append(person_dic_2)

# ensure that information is stored
# print(people)

# for person in people:
#     name = person["first name"]+person["last name"]
#     age = person["age"]
#     city = person["city"]
#
#     print("name: " + name + " age: " + age + " city: " + city)


# Page-99（6-8）
# Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary,
# include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next,
# loop through your list and as you do print everything you know about each pet.


# pets = []
#
# dog = {
#     "name": "lifugui",
#     "age": "2",
#     "weight": "20kg",
#     "color": "dark"
# }
#
# cat = {
#     "name": "mimi",
#     "age": "3",
#     "weight": "2kg",
#     "color": "white"
# }
#
# pig = {
#     "name": "zhutou",
#     "age": "1",
#     "weight": "30kg",
#     "color": "red"
# }
#
# pets.append(dog)
# pets.append(cat)
# pets.append(pig)
#
# for pet in pets:
#     name = pet["name"]
#     age = pet["age"]
#     weight = pet["weight"]
#     color = pet["color"]
#
#     print("name: " + name + " age: " + age + " weight: " + weight + " color: " + color)


# Page-99（6-9）
# Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary,
# and store one to three favorite places for each person. To make this exericse a bit more interesting,
# ask some friends to name a few of their favorite places. Loop through the dictionary,
# and print each person’s name and their favorite places.


# favorite_places = {
#     "jason": ["home", "gym"],
#     "henry": ["outside", "KFC"],
#     "tom": ["park", "peking opera"],
# }
#
# for name, places in favorite_places.items():
#     for place in places:
#         print(name.title() + " like " + place.title())


# Page-99（6-9）
# Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number.
# Then print each person’s name along with their favorite numbers.


# favorite_numbers = {
#     "Jason": ["33", "12"],
#     "Jerry": ["22", "4", "6"],
#     "Jeff": ["11", "7", "8"],
#     "Harry": ["00", "54"],
#     "Tom": ["88", "12", "32"]
# }
#
# for name, numbers in favorite_numbers.items():
#     for number in numbers:
#         print(name + " like " + number)


# Page-99（6-10）
# Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include the country that the city is in,
# its approximate population, and one fact about that city. The keys for each city’s dictionary should be something
# like country, population, and fact. Print the name of each city
# and all of the information you have stored about it.


cities = {
    "chengdu": {"country": "China", "population": "6158080", "economics": "A"},
    "shanghai": {"country": "China", "population": "7158080", "economics": "AA"},
    "beijing": {"country": "China", "population": "5158080", "economics": "AAA"}
}

for city, city_info in cities.items():
    country = city_info["country"]
    population = city_info["population"]
    economics = city_info["economics"]
    print(city.title() + " " + country.upper() + " " + population + " " + economics)






