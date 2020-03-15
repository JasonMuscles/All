# Page-87（6-1）
# Use a dictionary to store information about a person you know. Store their first name, last name, age,
# and the city in which they live. You should have keys such as first_name, last_name, age, and city.
# Print each piece of information stored in your dictionary.


# person_dic = {"first name": "jason",
#               "last name": "wang",
#               "age": "31",
#               "city": "CD"}
#
# print(person_dic["first name"])
# print(person_dic["last name"])
# print(person_dic["age"])
# print(person_dic["city"])


# Page-87（6-2）
# Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary.
# Think of a favorite number for each person, and store each as a value in your dictionary.
# Print each person’s name and their favorite number. For even more fun,
# poll a few friends and get some actual data for your program.


# favorite_numbers = {
#     "Jason": "33",
#     "Jerry": "22",
#     "Jeff": "11",
#     "Harry": "00",
#     "Tom": "88",
# }
#
# num = favorite_numbers["Jason"]
# print("Jason like number " + num)
#
# num = favorite_numbers["Jerry"]
# print("Jerry like number " + num)
#
# num = favorite_numbers["Jeff"]
# print("Jeff like number " + num)
#
# num = favorite_numbers["Harry"]
# print("Harry like number " + num)
#
# num = favorite_numbers["Tom"]
# print("Tom like number " + num)


# Page-87（6-3）
# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# •	Think of five programming words you’ve learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.
# •	Print each word and its meaning as neatly formatted output.
# You might print the word followed by a colon and then its meaning,
# or print the word on one line and then print its meaning indented on a second line.
# Use the newline character ('\n') to insert a blank line between each word-meaning pair in your output.


python_words = {
    "for": "循环",
    "in": "判断是否存在",
    "if": "判断",
    "=": "赋值",
    "!=": "不等",
    "==": "判断是否相等",
}

print("for :" + python_words["for"])
print("in :" + python_words["in"])
print("if :" + python_words["if"])
print("= :" + python_words["="])
print("!= :" + python_words["!="])
print("== :" + python_words["=="])

