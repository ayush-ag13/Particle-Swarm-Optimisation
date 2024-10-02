import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D

def create_triple_animation(optimizer, bounds, interval=100, save_gif=False):
    fig = plt.figure(figsize=(20, 7))
    
    # 3D merged view
    ax1 = fig.add_subplot(131, projection='3d')
    x = np.linspace(bounds[0][0], bounds[0][1], 100)
    y = np.linspace(bounds[1][0], bounds[1][1], 100)
    X, Y = np.meshgrid(x, y)
    Z = optimizer.objective_function(X, Y)
    surf = ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Fitness')
    ax1.set_title('3D Merged View')
    particles_scatter1 = ax1.scatter([], [], [], color='red', s=20, marker='o')
    global_best_scatter1 = ax1.scatter([], [], [], color='gold', s=100, marker='*')
    
    # 3D unmerged view
    ax2 = fig.add_subplot(132, projection='3d')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Fitness')
    ax2.set_title('3D Unmerged View')
    ax2.set_xlim(bounds[0])
    ax2.set_ylim(bounds[1])
    z_min, z_max = np.min(Z), np.max(Z)
    ax2.set_zlim(z_min, z_max)
    particles_scatter2 = ax2.scatter([], [], [], color='red', s=20, marker='o')
    global_best_scatter2 = ax2.scatter([], [], [], color='gold', s=100, marker='*')
    
    # 2D global best progression
    ax3 = fig.add_subplot(133)
    ax3.set_xlabel('Iteration')
    ax3.set_ylabel('Global Best Fitness')
    ax3.set_title('Global Best Progression')
    line, = ax3.plot([], [])
    minima_text = ax3.text(0.02, 0.98, '', transform=ax3.transAxes, verticalalignment='top')
    
    def init():
        particles_scatter1._offsets3d = ([], [], [])
        global_best_scatter1._offsets3d = ([], [], [])
        particles_scatter2._offsets3d = ([], [], [])
        global_best_scatter2._offsets3d = ([], [], [])
        line.set_data([], [])
        minima_text.set_text('')
        return particles_scatter1, global_best_scatter1, particles_scatter2, global_best_scatter2, line, minima_text

    def update(frame):
        # Update 3D views
        particle_positions = [optimizer.history[particle.hash][frame] for particle in optimizer.particles]
        x_vals = [pos[0] for pos in particle_positions]
        y_vals = [pos[1] for pos in particle_positions]
        z_vals = [optimizer.objective_function(pos[0], pos[1]) for pos in particle_positions]
        
        particles_scatter1._offsets3d = (x_vals, y_vals, z_vals)
        particles_scatter2._offsets3d = (x_vals, y_vals, z_vals)
        
        if frame < len(optimizer.history[hash('global_best')]):
            global_best_pos = optimizer.history[hash('global_best')][frame]
            global_best_z = optimizer.objective_function(global_best_pos[0], global_best_pos[1])
            global_best_scatter1._offsets3d = ([global_best_pos[0]], [global_best_pos[1]], [global_best_z])
            global_best_scatter2._offsets3d = ([global_best_pos[0]], [global_best_pos[1]], [global_best_z])
        
        # Update 2D global best progression
        line.set_data(range(frame + 1), optimizer.global_best_history[:frame + 1])
        ax3.relim()
        ax3.autoscale_view()
        
        # Update real-time global minima text
        current_minima = min(optimizer.global_best_history[:frame + 1])
        minima_text.set_text(f'Current Minima: {current_minima:.2f}')
        
        return particles_scatter1, global_best_scatter1, particles_scatter2, global_best_scatter2, line, minima_text

    ani = FuncAnimation(fig, update, frames=range(optimizer.max_iterations),
                        init_func=init, blit=False, interval=interval)

    if save_gif:
        ani.save('pso_triple_animation.gif', writer=PillowWriter(fps=10))

    plt.tight_layout()
    plt.show()