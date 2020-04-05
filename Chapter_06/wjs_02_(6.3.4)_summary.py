# Page-92（6-4）
# Now that you know how to loop through a dictionary,
# clean up the code from Exercise 6-3 (page 102) by replacing your series of print statements with a loop
# that runs through the dictionary’s keys and values. When you’re sure that your loop works,
# add five more Python terms to your glossary. When you run your program again,
# these new words and meanings should automatically be included in the output.


python_words = {
    "for": "循环",
    "in": "判断是否存在",
    "if": "判断",
    "=": "赋值",
    "!=": "不等",
    "==": "判断是否相等",
}

for words, means in python_words.items():
    print("'" + words + "'的意义是: " + means)


# Page-93（6-5）
# Make a dictionary containing three major rivers and the country each river runs through.
# One key-value pair might be 'nile': 'egypt'.
# •	Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# •	Use a loop to print the name of each river included in the dictionary.
# •	Use a loop to print the name of each country included in the dictionary.


# rivers = {
#     'nile': 'egypt',
#     'mississippi': 'united states',
#     'fraser': 'canada',
#     'kuskokwim': 'alaska',
#     'yangtze': 'china',
#     }
#
# for river, country in rivers.items():
#     print("The " + river + "runs through " + country)
#
# for river in rivers:
#     print("river name：" + river)
#
# for country in rivers:
#     print("country name：" + country)


# Page-93（6-6）
# Use the code in favorite_languages.py (page 104).
# •	Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that are not.
# •	Loop through the list of people who should take the poll. If they have already taken the poll,
# print a message thanking them for responding. If they have not yet taken the poll,
# print a message inviting them to take the poll.


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
#
# coders = ["jen", "sarah", "edward", "phil", "Jason", "Tom", "Harry"]
#
# for coder in coders:
#     if coder.lower() in favorite_languages.keys():
#         print(str(coder.lower()) + " thanking them for responding")
#     else:
#         print(str(coder.lower()) + " inviting them to take the poll")









