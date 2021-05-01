import copy
import random


class Hat:
    def __init__(self, **kwargs):
        contents = ''
        for color, num in kwargs.items():
            contents += f'{color} ' * num
        self.contents = contents.split()

    def draw(self, amount):
        if (len(self.contents) < amount):
            return self.contents
        removed = []
        for _ in range(amount):
            random_ind = random.randint(0, len(self.contents) - 1)
            removed.append(self.contents.pop(random_ind))
        return removed


def run_single_experiment(hat, expected_balls, num_balls_drawn):
    hat_for_experiment = copy.deepcopy(hat)
    removed = hat_for_experiment.draw(num_balls_drawn)
    for color, num in expected_balls.items():
        count = removed.count(color)
        if count < num:
            return False
    return True


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    times = 0
    for _ in range(num_experiments):
        times += run_single_experiment(
            hat=hat, expected_balls=expected_balls, num_balls_drawn=num_balls_drawn)
    return times / num_experiments
