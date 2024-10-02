import random

class Particle:
    def __init__(self, num_variables, bounds):
        self.position = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(num_variables)]
        self.velocity = [random.uniform(-1, 1) for _ in range(num_variables)]
        self.best_position = self.position[:]
        self.best_fitness = float('inf')
        self.hash = hash(tuple(self.velocity) + tuple(random.random() for _ in range(10)))

    def evaluate(self, objective_function):
        return objective_function(*self.position)