from src.objective_functions import rastrigin
from src.pso import PSO
from visualizations.visualization import create_triple_animation


def main():
    num_particles = 30
    num_variables = 2
    bounds = [[-5.12, 5.12], [-5.12, 5.12]]  # Standard bounds for Rastrigin function
    max_iterations = 100

    optimizer = PSO(num_particles, num_variables, bounds, max_iterations, rastrigin)
    optimizer.optimize()

    print("Global best position: ", optimizer.global_best_position)
    print("Global best fitness: ", optimizer.global_best_fitness)

    create_triple_animation(optimizer, bounds, interval=100, save_gif=True)

if __name__ == "__main__":
    main()