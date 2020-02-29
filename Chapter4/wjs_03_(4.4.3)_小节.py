# Page-58（4-10）
# 切片：打印消息在使用切片来打印列表的前三个元素。
foods = ["egg", "rice", "noodle", "oil", "protein", "apple"]
# for food in foods[:3]:
#     print(food)

# 打印消息在使用切片来打印列表的中间的2个元素。
# for food in foods[2:4]:
#     print(food)

# 打印消息在使用切片来打印列表末尾的三个元素。
# for food in foods[-3:]:
#     print(food)


# Page-58（4-11）
# 你的披萨和我的披萨：在你完成练习编写程序中创建披萨列表的副本，并将其存储到变量friend_pizzas中在完成如下任务。
foods = ["rice", "noodle", "apple"]
friend_foods = foods[:]

# 在原有的披萨列表中，增加一个新的披萨。
foods.append("meat")


# 在列表friend_pizzas中添加另一种披萨。
friend_foods.append("orange")


# 核实你有两个不同的列表维持打印消息，在使用一个或循环来打印，一个列表打印消息，在使用一个for环来打印第二个列表，核实新增的披萨被添加到正确的列表中
print("我的食物：", foods)
print("朋友食物：", friend_foods)



