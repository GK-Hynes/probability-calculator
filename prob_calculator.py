import copy
import random

class Hat:
    def __init__(self, **kwargs):
        balls = []
        for key, value in kwargs.items():
            balls.extend([key for i in range(value)])
        self.contents = balls

    def draw(self, num):
        if num > len(self.contents):
            return self.contents
        else:
            random.shuffle(self.contents)
            return self.contents[-num:]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass

