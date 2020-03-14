# Page-18（2-1）
# 简单消息：将一条信息存储到变量中，再将其打印出来。
message = "Hello！big boy！"
print(message)

# Page-18（2-2）
# 多条简单信息：请一条信息存储到变量中将其打印出来，再将变量的值修改为一条新信息，并将其打印出来。
message1 = "Hello！big girl！"
print(message1)
message2 = message1 + "How are you"
print(message2)


# Page-23（2-3）
# 个性化消息：将用户的姓名存到一个变量中，并向该用户显示一条消息显示到消息应非常简单。如："How are you today？"
name = "Jason wang"
print(name + "！" + "How are you today？")

# Page-23（2-4）
# 调整名字的大小写：将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式，显示这个人名。
print("小写=>", name.lower())
print("大写=>", name.upper())
print("首字母大写=>", name.title())

# Page-24（2-5）
# 名言：找一句你钦佩的名言将这个人的名字和他的名言打出来。
name1 = "老子"
famous_said = '说过：\"有钱能使鬼推磨!\"'
print(name1 + famous_said)

# Page-24（2-6）
# 名言2：重复练习2-5，将名人的姓名存储在变量famous_person中，再创建需要显示的消息，并将存储在变量message中，然后打印这条消息。
famous_person = name1
message3 = famous_said
print(famous_person + famous_said)

# Page-24（2-7）
# 剔除人名中的空白：存储一个人名，并在其开头和末尾都包含一些空白字符，至少使用字符组合"\t","\n"各一次。
name_wrong = " Jason wang"
print("\t", name_wrong)
print("\n", name_wrong)
print("\n\t", name_wrong)

# 打印这个人名，以显示其开头然后分别使用剔除函数，对人名进行处理，并将结果打印出来。
print("去掉开头空白：", name_wrong.lstrip())
print("去掉末尾空白：", name_wrong.rstrip())
print("去掉开尾空白：", name_wrong.strip())

# Page-27（2-8）
# 数字8：编写四个表达式，他们分别使用加法减法乘法和除法运算，但结果都是数字八。
print(4 + 4)
print(8 - 4)
print(2 * 4)
print(80/10)

# Page-27（2-9）
# 最喜欢的数字:将你最喜欢的数字存储在一个变量中，在使用这个变量创建一条。消息指出你最喜欢的数字，然后将这条消息打印出来。
favorite_num = 33
print("my favorite number:" + str(favorite_num))

# Page-28（2-10）
# 添加注释


def mystrip():
    """
    自定义一个strip去掉收尾空白
    """
    print(name_wrong.strip())
    return None


if __name__ == '__main__':
    mystrip()

# Page-29（2-11）
# Python指导原则 import this
import this

