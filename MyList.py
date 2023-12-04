import random


class MyList(list):
    def choice(self):
        return random.choice(self)


ls = MyList([1, 2, 5, 4, 9, 7, 8])
print(ls.choice())
