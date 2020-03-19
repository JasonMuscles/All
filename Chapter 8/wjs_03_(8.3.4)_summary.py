# Page-125（8-6）
# Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted like this:“Santiago, Chile”
# Call your function with at least three city-country pairs, and print the value that’s returned.


# def city_country(city, country):
#
#     return city.title(), country.title()
#
#
# city1 = city_country("beijing", "china")
# print(city1)


# Page-125（8-7）
# Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title, and it should return a dictionary containing
# these two pieces of information. Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album information correctly.
# Add an optional parameter to make_album() that allows you to store the number of tracks on an album.
# If the calling line includes a value for the number of tracks, add that value to the album’s dictionary.
# Make at least one new function call that includes the number of tracks on an album.


# def make_album(artist_name, album_title):
#
#     music_album = {
#         "artist_name": artist_name,
#         "album_title": album_title
#         }
#
#     return music_album
#
#
# album = make_album("jason", "bird")
# print(album)
#
# album = make_album("jason1", "bird1")
# print(album)
#
# album = make_album(album_title="jason", artist_name="bird")
# print(album)

# ==============================================================================================

# def make_album(artist_name, album_title, tracks=0):
#
#     music_album_dict = {
#         "artist_name": artist_name,
#         "album_title": album_title
#         }
#
#     if tracks:
#         music_album_dict["tracks"] = tracks
#
#     return music_album_dict
#
#
# album = make_album("jason", "bird")
# print(album)
#
# album = make_album("jason1", "bird1")
# print(album)
#
# album = make_album(album_title="jason", artist_name="bird", tracks=0)
# print(album)


# Page-126（8-8）
# Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title.
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
# Be sure to include a quit value in the while loop.


def make_album(artist_name, album_title, tracks=0):

    music_album_dict = {
        "artist_name": artist_name,
        "album_title": album_title
        }

    if tracks:
        music_album_dict["tracks"] = tracks

    return music_album_dict


prompt_artist_name = "\ninput artist name："
prompt_album_title = "\ninput album title："

# print("Enter 'quit' at any time to stop. ")

while True:
    print("Enter 'quit' at any time to stop. ")

    title = input(prompt_artist_name)
    if title == "quit":
        break

    name = input(prompt_album_title)
    if name == "quit":
        break

    album = make_album(name, title)

    print(album)

print("\nThanks for responding!")






