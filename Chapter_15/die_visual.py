from Chapter_15.die import Die
import pygal

# 创建一个D6
die = Die()

# 投掷几次骰子，并将结果存储在一个列表中
results = []

for roll_num in range(10000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对比可视化结果
hist = pygal.Bar()

hist.title = "10000 times D6"
hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist.y_labels = "Result"
hist.y_labels = "Frequency of Result"

hist.add("D6", frequencies)
hist.render_to_file("die_visual.svg")




