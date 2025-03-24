import numpy as np
import matplotlib.pyplot as plt

def draw_spiral_to_top(circle_radius, turns):
    """
    Draws an Archimedean spiral from the center to the top of the circle.

    Args:
        circle_radius: Radius of the circle.
        turns: Desired number of turns for the spiral.
    """

    if turns <= 0:
        print("Number of turns must be positive.")
        return

    final_theta = turns * 2 * np.pi # End at top (pi/2 radians)
    spiral_constant = circle_radius / final_theta

    theta = np.linspace(0, final_theta, 1000) #- np.pi / 2
    r = spiral_constant * theta

    y = - r * np.cos(theta)
    x = r * np.sin(theta)

    # Draw the circle
    circle_theta = np.linspace(0, 2 * np.pi, 100)
    circle_x = circle_radius * np.cos(circle_theta)
    circle_y = circle_radius * np.sin(circle_theta)

    # Plot
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label="Spiral")
    plt.plot(circle_x, circle_y, 'r--', label="Circle")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Spiral to Top of Circle")
    plt.axis("equal")
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"Number of Turns: {turns:.2f}")

# Example usage:
circle_radius = 10
turns = 3.5
draw_spiral_to_top(circle_radius, turns)

