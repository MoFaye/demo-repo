import numpy as np


class adding_nums:
    def __init__(self, a, b):
        self.first_num = a
        self.second_num = b

    def add(self):
        self.add = self.first_num + self.second_num
        print(self.add)


if __name__ == "__main__":
    f = adding_nums(5,6)
    f.add()