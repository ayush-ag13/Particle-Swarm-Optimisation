# Particle Swarm Optimization (PSO) Visualization

This repository contains a Python implementation of Particle Swarm Optimization (PSO) with visualization capabilities. The project demonstrates PSO on the Rastrigin function, a common benchmark problem in optimization.

## What is Particle Swarm Optimization?

Particle Swarm Optimization (PSO) is a population-based optimization technique inspired by the social behavior of birds flocking or fish schooling. Developed by Kennedy and Eberhart in 1995, PSO is particularly effective in solving continuous and discrete optimization problems.

Key concepts in PSO:

1. **Particles**: Each potential solution is represented as a particle in the search space.
2. **Velocity**: Particles move through the solution space with a velocity, which is adjusted based on the particle's own experience and the experience of its neighbors.
3. **Personal Best**: Each particle remembers the best position it has encountered.
4. **Global Best**: The best position found by any particle in the swarm.

In each iteration, particles adjust their velocities and positions based on their personal best and the global best, gradually converging towards the optimal solution.

## How PSO is Applied in This Project

In this implementation, we apply PSO to the Rastrigin function, a common benchmark problem in optimization. Here's how the algorithm is applied:

1. **Initialization**: We create a swarm of particles, each representing a potential solution in the 2D space of the Rastrigin function.

2. **Objective Function**: The Rastrigin function serves as our objective function. It's characterized by many local minima, making it a challenging optimization problem.

3. **Particle Movement**: In each iteration, particles move through the solution space, adjusting their velocities based on:
   - Inertia: A portion of their previous velocity
   - Cognitive component: Attraction towards their personal best position
   - Social component: Attraction towards the global best position

4. **Update Best Positions**: After each move, we update the personal best for each particle and the global best for the swarm if better positions are found.

5. **Visualization**: We provide real-time visualization of the optimization process, showing:
   - 3D view of particles moving on the Rastrigin function surface
   - 2D view of particles' positions
   - Progress of the global best fitness over iterations

This implementation allows users to observe how PSO navigates the complex landscape of the Rastrigin function, avoiding local minima and converging towards the global minimum.

## Project Structure

```
particle-swarm-optimization/
│
├── src/
│   ├── __init__.py
│   ├── particle.py
│   ├── pso.py
│   └── objective_functions.py
│
├── visualizations/
│   └── visualization.py
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/particle-swarm-optimization.git
   cd particle-swarm-optimization
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the main script to start the PSO algorithm and generate visualizations:

```
python main.py
```

This will run the PSO algorithm on the Rastrigin function and create an animated visualization of the optimization process.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

