from tqdm import tqdm
from .particle import Particle

class PSO:
    def __init__(self, num_particles, num_variables, bounds, max_iterations, objective_function):
        self.inertia_weight = 0.5
        self.cognitive_weight = 1.5
        self.social_weight = 1.5
        self.num_particles = num_particles
        self.num_variables = num_variables
        self.bounds = bounds
        self.max_iterations = max_iterations
        self.objective_function = objective_function
        self.global_best_position = [0.0] * num_variables
        self.global_best_fitness = float('inf')
        self.particles = [Particle(num_variables, bounds) for _ in range(num_particles)]

        self.history = {particle.hash: [particle.position[:]] for particle in self.particles}
        self.history[hash('global_best')] = []
        self.global_best_history = []

    def optimize(self):
        for _ in tqdm(range(self.max_iterations)):
            for particle in self.particles:
                fitness = particle.evaluate(self.objective_function)
                if fitness < particle.best_fitness:
                    particle.best_fitness = fitness
                    particle.best_position = particle.position[:]
                if fitness < self.global_best_fitness:
                    self.global_best_fitness = fitness
                    self.global_best_position = particle.position[:]
            self.history[hash('global_best')].append(self.global_best_position[:])
            self.global_best_history.append(self.global_best_fitness)

            for particle in self.particles:
                self.update_particle(particle)

    def update_particle(self, particle):
        for i in range(self.num_variables):
            r1, r2 = random.random(), random.random()
            particle.velocity[i] = (self.inertia_weight * particle.velocity[i] +
                                    self.cognitive_weight * r1 * (particle.best_position[i] - particle.position[i]) +
                                    self.social_weight * r2 * (self.global_best_position[i] - particle.position[i]))
            particle.position[i] += particle.velocity[i]
            particle.position[i] = max(min(particle.position[i], self.bounds[i][1]), self.bounds[i][0])
        self.history[particle.hash].append(particle.position[:])