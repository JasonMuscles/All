# Page-38（3-4）
# 嘉宾名单：创建4个人的名单，并以此列表名单打印邀请消息。
gustes = ["jason", "tom", "jerry", "marry"]
print(gustes)

# Page-38（3-5）
# 修改嘉宾名单：打印出无法参加的人名单。
gustes_not_come = gustes.pop(0)
print("无法赴约人员: " + gustes_not_come.title())
print("目前能赴约人员: " + str(gustes).title())

# 替换无法赴约的嘉宾名字，为新嘉宾名字。
gustes.append("harry")

# 更新名单后向此列表名单人员发出邀请消息。
gustes_new = gustes
print("新赴约名单：" + str(gustes_new))

# Page-38（3-6）
# 添加新嘉宾名单到名单第一位，insert。
gustes_new.insert(0, "peter")
print(gustes_new)

# insert新嘉宾到名单中间。
gustes_new.insert(2, "jeff")
print(gustes_new)

# 更新名单后向此列表名单人员发出邀请消息。
print("新赴约名单：" + str(gustes_new))

# Page-38（3-7）
# 缩减名单，pop，直到只有两位宾客。
print("不要你来了：" + str(gustes_new.pop(-1)))
print("不要你来了：" + str(gustes_new.pop(-1)))
print("不要你来了：" + str(gustes_new.pop(-1)))
print("不要你来了：" + str(gustes_new.pop(-1)))

# 余下嘉宾都邀请
print("过来Hi: " + gustes_new[0])
print("过来Hi: " + gustes_new[1])

# 使用del删除掉最后两名
del gustes_new[-1]
del gustes_new[-1]
print("还有人没有：" + str(gustes_new))
