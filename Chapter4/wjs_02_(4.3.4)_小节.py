# Page-54（4-3）
# 使用一个for循环打印数字一到20（含20）。
# for num in range(1, 21):
#     print(num)

# Page-54（4-4）
# 一百万：创建一个列表，其中包含数字1到1,000,000在使用一个或循环，将这些数字打印出来。
# numbers = []
# for value in range(1, 1000001):
#     numbers.append(value)
# print(numbers)

# Page-54（4-5）
# 计算1到1,000,000的总和。
# numbers = []
# for value in range(1, 1000001):
#     numbers.append(value)
# print(sum(numbers))

# Page-54（4-6）
# 通过给函数range指定第3个参数来创建一个列表，其中包含1到20的奇数，在使用一个或循环中，这些数字都打印出来。
# for c in range(1, 21, 2):
#     print(c)

# 3的倍数创建一个列表，其中包含3到30名能被三整除的数字，在使用一个或循环将这些列表中的数字都打印出来。
# for c in range(3, 31, 3):
#     print(c)

# 立方：将同一个数字乘以3次成为立方，请创建一个列表，其中包含前10个整数，即到10的立方在使用一个或循环，将这些地方都打印出来。
# cube = []
# for values in range(1, 11):
#     cube = values ** 3
#     print(cube)


# 立方解析：使用列表解析生成一个列表，其中包含前10个整数的立方。
lists = [values ** 3 for values in range(1, 11)]
print(lists)



