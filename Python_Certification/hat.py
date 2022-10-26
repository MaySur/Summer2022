import random


class Hat:
    houses = ['Grif', 'Huff', 'Raven', 'Slyt']

    @classmethod
    def sort(cls, name):
        print(name, 'is in ', random.choice(cls.houses))



Hat.sort('Harry')