import matplotlib.pyplot as plt
from Chapter_15.Random_Walk import RandomWalk

"""只要程序处于活动状态，就不断的模拟随机漫步"""

while True:
    """创建一个Random实例，并将其包含的点都绘制出来"""
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.get_cmap('PuBuGn_r'), edgecolors="none", s=5)

    # 突出起点和终点
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # 隐藏坐标轴
    plt.xticks([])
    plt.yticks([])

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break