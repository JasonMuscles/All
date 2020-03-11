# Page-70（5-1）
# 编写一系列条件测试测试，将每一测试以及结果的预测和实际结果都打印出来。
# name = "jason"
# print("you name == 'jason'? I predict true.")
# print(name == "jason")

# Page-70（5-2）
# 检查两个字符串相等和不等。
value = "qwertyui"
value2 = "Gwertyui"
# print(value == value2)

# 使用函数lower()测试。
print(value2.lower() == "gwertyui")

# 检查两个数字相等，不等大于小于大于等于和小于等于。
var1 = 1
var2 = 2
var3 = 1
var4 = 5
print("相等：", var1 == var3)
print("大于：", var2 > var1)
print("小于：", var1 < var4)
print("不等：", var1 != var4)
print("大于等于：", var1 <= var3)
print("小于等于：", var1 >= var3)

# 使用关键字and和or测试。
print((var1 == var3) and (var2 > var1))
print((var1 != var3) and (var2 > var1))

print((var1 != var3) or (var2 < var1))
print((var1 != var3) or (var2 > var1))

# 测试特定的值是否包含在列表中。
list_new = ["a", "b", "c", "d"]
print("a" in list_new)


# 测试特定的值是否未包含在列表中。
list_new = ["a", "b", "c", "d"]
print("e" in list_new)






