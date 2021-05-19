import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num_to_draw):
        if num_to_draw > len(self.contents):
            return self.contents
        else:
            drawn_balls = []
            for i in range(num_to_draw):
                selected_ball = random.choice(self.contents)
                drawn_balls.append(selected_ball)
                self.contents.remove(selected_ball)
            return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # How many times you got expected_balls
    successes = 0

    # Run experiments
    for experiment in range(num_experiments):
        # Make copies of hat and expected_balls so as not to influence next experiment
        copied_hat = copy.deepcopy(hat)
        copied_expected = copy.deepcopy(expected_balls)

        # Draw
        drawn_balls = copied_hat.draw(num_balls_drawn)

        # Compare copies
        for ball in drawn_balls:
            if ball in copied_expected:
                copied_expected[ball] -= 1
        if all (value <= 0 for value in copied_expected.values()):
            successes += 1
        
    return successes/num_experiments

