import numpy as np
import matplotlib.pyplot as plt

def draw_and_diffuse_spiral(circle_radius, turns, diffusion_radius=0.5):
    """
    Draws an Archimedean spiral and simulates color diffusion.

    Args:
        circle_radius: Radius of the circle.
        turns: Number of turns for the spiral.
        diffusion_radius: Radius of the color diffusion at each point.
    """

    final_theta = turns * 2 * np.pi
    spiral_constant = circle_radius / final_theta

    theta = np.linspace(0, final_theta, 1000)
    r = spiral_constant * theta

    x = r * np.sin(theta)
    y = - r * np.cos(theta)

    # Draw the circle
    circle_theta = np.linspace(0, 2 * np.pi, 100)
    circle_x = circle_radius * np.cos(circle_theta)
    circle_y = circle_radius * np.sin(circle_theta)

    # Plot
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label="Spiral")
    plt.plot(circle_x, circle_y, 'r--', label="Circle")

    # Simulate color diffusion
    for i in range(len(x)):
        diffusion_circle_theta = np.linspace(0, 2 * np.pi, 50)
        diffusion_x = x[i] + diffusion_radius * np.cos(diffusion_circle_theta)
        diffusion_y = y[i] + diffusion_radius * np.sin(diffusion_circle_theta)
        plt.plot(diffusion_x, diffusion_y, 'g-', linewidth=0.1) # 'g-' for green, very thin line.

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Spiral with {turns:.2f} Turns and Diffusion")
    plt.axis("equal")
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage and experimentation:
# circle_radius = 10
#
# diffusion_radius = 1.0 #experiment with larger diffusion radius
# for turns in turns_values:
#     draw_and_diffuse_spiral(circle_radius, turns, diffusion_radius)
#
# diffusion_radius = 0.25 #experiment with smaller diffusion radius
# for turns in turns_values:
#     draw_and_diffuse_spiral(circle_radius, turns, diffusion_radius)

circle_radius = 7*np.pi
diffusion_radius = np.pi  # Adjust to change diffusion size

# Experiment with different numbers of turns:
turns_values = [1.5, 2.5, 3.5, 4.5]

for turns in turns_values:
    draw_and_diffuse_spiral(circle_radius, turns, diffusion_radius)

# This shows that only at 3.5 turns, the circle is completely filled without overlaps (except for the first half turn).
# Assuming b = 1, each full spiral increase radius/distance by 2pi. So you want the diffusion to be half of this, which is pi. So pranava is spread throughout the AdiValaya.
# Again if radius is 7*pi, 3.5 turns is ideal. But if it's 9pi, then 4.5 turns will be ideal. So still doesn't exactly tell why 3.5 turns.