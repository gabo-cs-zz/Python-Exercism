import random
from string import ascii_uppercase as alph
from string import digits as numbers


class Robot:
    def __init__(self):
        self.name = self.__random_name()

    def random_name(self):
        return self.__random_values(alph, 2) + self.__random_values(numbers, 3)

    def random_values(self, collection, length):
        return ''.join(random.choice(collection) for i in range(length))

    def reset(self):
        random.seed()
        self.name = self.__random_name()

    __random_name = random_name
    __random_values = random_values
