import random


def draw():
    return random.randint(1, 11)


class Dealer():
    def __init__(self):
        self.hand = random.randint(1, 11)
