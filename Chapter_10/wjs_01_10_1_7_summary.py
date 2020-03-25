# Page-169（10-1）
# Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far.
# Start each line with the phrase In Python you can… Save the file as learning_python.txt in the same directory as your
# exercises from this chapter. Write a program that reads the file and prints what you wrote three times.
# Print the contents once by reading in the entire file, once by looping over the file object,
# and once by storing the lines in a list and then working with them outside the with block.

# file_path = "learning_python.txt"
#
#
# print("--- Reading in the entire file:")
# with open(file_path) as file_object:
#     contents = file_object.read()
# print(contents)


# print("\n--- Looping over the lines:")
# with open(file_path) as f:
#     for line in f:
#         print(line.rstrip())


# print("\n--- Storing the lines in a list:")
# with open(file_path) as f:
#     lines = f.readlines()
#
# for line in lines:
#     print(line.rstrip())


# Page-169（10-2）
# You can use the replace() method to replace any word in a string with a different word. Here’s a quick example
# showing how to replace 'dog' with 'cat' in a sentence:>>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')'I really like cats.'Read in each line from the file you just created,
# learning_python.txt, and replace the word Python with the name of another language, such as C.
# Print each modified line to the screen.


file_path = "learning_python.txt"

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip().replace("Python", "C"))





