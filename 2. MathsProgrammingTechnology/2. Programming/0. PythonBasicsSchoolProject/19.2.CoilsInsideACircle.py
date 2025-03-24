import numpy as np
import matplotlib.pyplot as plt

def draw_spiral_in_circle(circle_radius, spiral_constant, initial_radius=0):
    """
    Draws an Archimedean spiral within a circle.

    Args:
        circle_radius: Radius of the circle.
        spiral_constant: Constant 'b' in the spiral equation r = a + b*theta.
        initial_radius: Initial radius 'a' (default is 0).
    """

    theta = np.linspace(0, 100, 1000)  # Generate angles
    r = initial_radius + spiral_constant * theta  # Calculate spiral radius

    # Limit the spiral to the circle's radius
    valid_indices = r <= circle_radius
    theta = theta[valid_indices]
    r = r[valid_indices]

    # x = r * np.cos(theta)  # Convert polar to Cartesian coordinates
    # y = r * np.sin(theta)

    # rotating it so we can go from bottom to top
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
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Archimedean Spiral in a Circle")
    plt.axis("equal")  # Ensure equal aspect ratio
    plt.legend()
    plt.grid(True)
    plt.show()

    # Calculate number of turns
    if spiral_constant !=0:
        final_theta = (circle_radius - initial_radius) / spiral_constant
        turns = final_theta / (2 * np.pi)
        print(f"Number of Turns: {turns:.2f}")
    else:
        print("Spiral Constant cannot be zero.")

# Example usage:
# circle_radius = 10
# spiral_constant = 0.5
# initial_radius = 0 #try changing this to non zero numbers.
# draw_spiral_in_circle(circle_radius, spiral_constant, initial_radius)
#
# circle_radius = 10
# spiral_constant = 1
# initial_radius = 2
# draw_spiral_in_circle(circle_radius, spiral_constant, initial_radius)
#
# circle_radius = 15
# spiral_constant = 0.25
# initial_radius = 0
# draw_spiral_in_circle(circle_radius, spiral_constant, initial_radius)

# R/(2*b*pi) = NTurns = 3.5 => b = R/(7*pi)
circle_radius = 7
spiral_constant = 1/np.pi
initial_radius = 0
draw_spiral_in_circle(circle_radius, spiral_constant, initial_radius)
    # here each spiral from center to the top is at a distance of 1, 3, 5, 7

# If we add initial radius - not helpful
# R/(2*b*pi) = NTurns = 3.5 => b = R/(7*pi)
circle_radius = 7
spiral_constant = 1/np.pi
initial_radius = 1
draw_spiral_in_circle(circle_radius, spiral_constant, initial_radius)

# Assume pi is 22/7 -- NTurns = R/(2*b*pi) = R/(2*b*22/7) = 3.5*R/(22*b)
circle_radius = 22
spiral_constant = 1
initial_radius = 0
draw_spiral_in_circle(circle_radius, spiral_constant, initial_radius)
### N = R/(2*b*pi), so pi = R/(2*b*N) ==> if 'b' is 1, each pi radians, you are increasing radius by 1.

# Same as before but changing b = 1 instead of 1/pi, and not using approximation of pi
# R/(2*b*pi) = NTurns = 3.5 => b = R/(7*pi)
circle_radius = 7*np.pi
spiral_constant = 1
initial_radius = 0
draw_spiral_in_circle(circle_radius, spiral_constant, initial_radius)


# Trying to match Shri Mataji's text in Her Creation book
# Let's say circumference is 22, diameter is 7. So radius is 3.5
# R/(2*b*pi) = NTurns = 3.5 => b = R/(7*pi)
circle_radius = 3.5
spiral_constant = 1/(2*np.pi)
initial_radius = 0
draw_spiral_in_circle(circle_radius, spiral_constant, initial_radius)
# So, each full spiral here (for 2pi angle) increases the radius by 1. So for half the diameter or the full radius (3.5), you will need 3.5 turns. Alternatively, if we scale b by 2pi, then each half spiral is is increasing the radius by pi - so we may 'call it pi'?
# For 3.5 spirals, we do get 7 intersections or 7 times the spiral distance b*2pi - across the diameter
# Alternatively, if b = 1, then each half turn is pi. If we want 7 segments, it will be 3.5 coils. But this still doesn't explain why 3.5 or 7?
# Or could this be a maximization/minimization problem? What are we maximizing/minimizing?
# See also how Ellipse/Valaya is changed to heart shape first, and then the waves off Pranava pulsate around in 3 and half coils.. creating the coil .. if they are going outwardly, may be towards the Adivalaya circle from before the stage of Bindu and Valaya. May be when Aum is formed after Sadashiva pushes Her and himself away, but it's all still inside the Adivalaya, so the emitted waves pulsate to the Adivalaya?
# Note that it is creating a heart shape for the central half spiral - from the heart the spiral waves are emanating to the AdiValaya? (See the code versions with diffusion around the spiral - in a way to spread pranava all over inside the Adivalaya
# Next step would be to simulate all of this - starting from Adivalaya, to Bindu + Valaya to then the formation of Aum, and then the outward coils emanating Pranava to the Adivalaya..