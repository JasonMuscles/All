# Page-41（3-8）
# 放眼世界：五个旅游景点，且字母都不是按顺序排列的。
travel_address = ["d", "c", "s", "x", "a", "b"]

# 打印景点
print(travel_address)

# 使用sorted，打印
print(sorted(travel_address))

# 核实原有顺序未改变
print(travel_address)

# 使用sorted，按照与字母相反的顺序打印出来，同时不要修改他。
print(sorted(travel_address, reverse=True))

# 核实原有顺序未改变
print(travel_address)

# 使用reverse()修改列表人数的排列顺序，并的应该列表，何时排列顺序，确实已进行了改变。
travel_address.reverse()
print(travel_address)

# 使用reverse()修改列表人数的排列顺序，使之恢复之前原有顺序
travel_address.reverse()
print(travel_address)

# 使用sort修改一个列表元素，按照字母排序，并打印核实顺序已改变。
travel_address.sort()
print(travel_address)

# 使用sort修改一个列表元素，按照反向字母排序，并打印核实顺序已改变。
travel_address.sort(reverse=True)
print(travel_address)

# 有多少个旅游地方
print(len(travel_address))




