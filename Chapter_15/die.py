from random import randint


class Die():
    """一个骰子的类"""
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """返回一个1-6的随机值"""
        return randint(1, self.num_sides)

