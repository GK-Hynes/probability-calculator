import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents.extend([key for i in range(value)])

    def draw(self, num):
        if num > len(self.contents):
            return self.contents
        else:
            drawn = []
            for i in range(num):
                selected = random.choice(self.contents)
                self.contents.remove(selected)
                drawn.append(selected)
            return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass

