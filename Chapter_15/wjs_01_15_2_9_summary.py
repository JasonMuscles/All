# Page-295（15-1）
# A number raised to the third power is a cube. Plot the first five cubic numbers,
# and then plot the first 5000 cubic numbers.


# from matplotlib import pyplot as plt
#
# # Define data.
# x_values = [1, 2, 3, 4, 5]
# cubes = [1, 8, 27, 64, 125]
#
# # Make plot.
# plt.scatter(x_values, cubes, edgecolor='none', s=40)
#
# # Customize plot.
# plt.title("Cubes", fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Cube of Value', fontsize=14)
# plt.tick_params(axis='both', labelsize=14)
#
# # Show plot.
# plt.show()

# from matplotlib import pyplot as plt
#
# # Define data.
# x_values = list(range(5001))
# cubes = [x**3 for x in x_values]
#
# # Make plot.
# plt.scatter(x_values, cubes, edgecolor='none', s=40)
#
# # Customize plot.
# plt.title("Cubes", fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Cube of Value', fontsize=14)
# plt.tick_params(axis='both', labelsize=14)
# plt.axis([0, 5100, 0, 5100**3])
#
# # Show plot.
# plt.show()


# Page-295（15-1）
# Apply a colormap to your cubes plot.


from matplotlib import pyplot as plt

# Define data.
x_values = list(range(5001))
cubes = [x**3 for x in x_values]

# Make plot.
plt.scatter(x_values, cubes, edgecolor='none', c=cubes, cmap=plt.cm.BuGn, s=40)

# Customize plot.
plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 5100, 0, 5100**3])

# Show plot.
plt.show()


