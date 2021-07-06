import random

class Dice:

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def roll(self):
        return random.randint(self.min_value, self.max_value)


class Player:

    def __init__(self, name):
        self.name = name
        self.position = 1
        self.won = False
    

class Board:

    def __init__(self, size):
        self.size = size
        self.start = 1
        self.end = size

class Snake:

    def __init__(self, start, end):
        self.start = start
        self.end = end


        
    