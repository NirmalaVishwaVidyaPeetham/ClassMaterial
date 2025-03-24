import numpy as np
import matplotlib.pyplot as plt

def draw_spiral_in_circle(circle_radius, spiral_constant, initial_radius=0, diffusion_radius=0.25):
    """
    Draws an Archimedean spiral within a circle and simulates color diffusion.

    Args:
        circle_radius: Radius of the circle.
        spiral_constant: Constant 'b' in the spiral equation r = a + b*theta.
        initial_radius: Initial radius 'a' (default is 0).
        diffusion_radius: Radius of the color diffusion at each point.
    """

    theta = np.linspace(0, 100, 1000)  # Generate angles
    r = initial_radius + spiral_constant * theta  # Calculate spiral radius

    # Limit the spiral to the circle's radius
    valid_indices = r <= circle_radius
    theta = theta[valid_indices]
    r = r[valid_indices]

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
        plt.plot(diffusion_x, diffusion_y, 'g-', linewidth=0.2)

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Archimedean Spiral in a Circle")
    plt.axis("equal")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Calculate number of turns
    if spiral_constant != 0:
        final_theta = (circle_radius - initial_radius) / spiral_constant
        turns = final_theta / (2 * np.pi)
        print(f"Number of Turns: {turns:.2f}")
    else:
        print("Spiral Constant cannot be zero.")

# Example usage:

circle_radius = 3.5
diffusion_radius = 0.5
spiral_constant = 1 / (2 * np.pi)
initial_radius = 0
draw_spiral_in_circle(circle_radius, spiral_constant, initial_radius, diffusion_radius)
# if radius is 3.5, 3.5 turns is ideal.But if it's 9, then 8 turns will be ideal. So still doesn't exactly tell why 3.5 turns.
# Note that it is creating a heart shape for the central half spiral - from the heart the spiral waves are emanating to the AdiValaya?
# If you want it go out starting from south angle to end at north angle, then you should have odd multiple of pi. Then if you want to go out as fast as possible, then it should be the smallest number of turns. This means it has to 1.5, 2.5, 3.5, 4.5 etc. - then what other criteria does 3.5 fill, that 1.5, 2.5, 4.5 don't? The angle of the central heart is different in each case, with 3.5 pointing leftwards. How about the total fraction of area that's covered inside the circle? Can we maximize that? Wouldn't 4.5 cover even more?