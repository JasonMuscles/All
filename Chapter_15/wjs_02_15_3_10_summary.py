# Page-303（15-3）
# Modify rw_visual.py by replacing plt.plot() with plt.plot(). to simulate the path of a pollen grain on
# the surface of a drop of water, pass in the rw.x_values and rw.y_values, and include a line width argument.
# Use 5000 instead of 50,000 points.

import matplotlib.pyplot as plt
from Chapter_15.Random_Walk import RandomWalk

"""只要程序处于活动状态，就不断的模拟随机漫步"""

while True:
    """创建一个Random实例，并将其包含的点都绘制出来"""
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # 突出起点和终点

    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # 隐藏坐标轴
    # 隐藏坐标轴
    plt.xticks([])
    plt.yticks([])

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break


# Page-303（15-4）
# The scatter plots appear behind the lines. To place them on top of the lines, we can use the zorderargument.
# Plot elements with higher zorder values are placed on top of elements with lowerzorder values.


"""只要程序处于活动状态，就不断的模拟随机漫步"""
while True:
    """创建一个Random实例，并将其包含的点都绘制出来"""
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)

    # 突出起点和终点

    plt.scatter(0, 0, c="green", edgecolors="none", s=100, zorder=2)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100, zorder=2)

    # 隐藏坐标轴
    # 隐藏坐标轴
    plt.xticks([])
    plt.yticks([])

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break


# Page-303（15-5）
# The method fill_walk() is lengthy. Create a new method called get_step() to determine the direction and distance
# for each step, and then calculate the step. You should end up with two calls to get_step() in fill_walk()
# :x_step = get_step() y_step = get_step() This refactoring should reduce the size of fill_walk() and make the method
# easier to read and understand.












