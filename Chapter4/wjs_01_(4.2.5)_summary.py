# Page-50（4-1）
# 三种食物存贮在一个列表中，并循环打印。
foods = ["rice", "noodle", "apple"]
for food in foods:
    print(food)

# 打印所有食物并输出一句话
for food in foods:
    print("我喜欢吃：" + food)

# 三种食物都输出，并在程序末尾输出最喜欢的食物
for food in foods:
    print("我喜欢这些食物：" + food + " ", end="")
print("\n但是我最喜欢的还是" + foods[2])

# Page-50（4-2）
# 三种动物的三种特征将其存储在一个列表中在使用循环将每个特征都打印出来。
animals = ["dog", "cat", "pig"]
for animal in animals:
    print(animal)

# 修改这个程序对每个动物都打印一个句子。
for animal in animals:
    print(animal + "是宠物")

# 在程序末尾增加一行代码，指出这些动物的共同之处。
print("都吃喝拉撒")