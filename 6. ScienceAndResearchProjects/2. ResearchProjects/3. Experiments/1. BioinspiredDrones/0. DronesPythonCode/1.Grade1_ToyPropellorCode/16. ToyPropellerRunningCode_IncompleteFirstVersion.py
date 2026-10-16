#Create a python model of a toy propellor. As the propellor is given an initial rotation, the air pushes it upwards, while gravity pulls it downwards. If the initial speed of rotation is greater than some value (beyond the force due to gravity), then it will go up. Gradually as the propellor slows down, it starts coming back down. Show the rotation of the propellor and it's vertical motion. At each point of time, also the values for upwards force and downwards force - Show these values in green if upwards > downwards, in red if upwards < downwards.


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import matplotlib.animation as animation

# Constants
GRAVITY = 9.8
AIR_DENSITY = 1.225
PROPELLER_RADIUS = 0.05
PROPELLER_MASS = 0.01
DRAG_COEFFICIENT = 0.5
LIFT_COEFFICIENT = 0.8

# Initial conditions
INITIAL_ROTATION_SPEED = 50.0
INITIAL_VERTICAL_POSITION = 0.0
INITIAL_VERTICAL_SPEED = 0.0

# Simulation parameters
TIME_STEP = 0.01
SIMULATION_DURATION = 5

# Lists to store data for plotting
time_values = []
position_values = []
rotation_angles = []
upward_force_values = []
downward_force_values = []

# Propeller properties
num_blades = 3
blade_length = PROPELLER_RADIUS * 0.8

# Initialize variables
rotation_speed = INITIAL_ROTATION_SPEED
vertical_position = INITIAL_VERTICAL_POSITION
vertical_speed = INITIAL_VERTICAL_SPEED
initial_lift_force = 0  # Store the initial lift force

# Simulation loop
time = 0
while time <= SIMULATION_DURATION:
    time_values.append(time)
    position_values.append(vertical_position)
    rotation_angles.append((rotation_speed * time) % (2 * np.pi))

    # Calculate forces (Lift force now only decreases)
    lift_force = 0.5 * AIR_DENSITY * (rotation_speed * PROPELLER_RADIUS)**2 * LIFT_COEFFICIENT * np.pi * PROPELLER_RADIUS**2
    if time == 0:  # Store initial lift
        initial_lift_force = lift_force

    lift_force = min(lift_force, initial_lift_force) # Lift can only decrease

    drag_force_magnitude = 0.5 * AIR_DENSITY * abs(vertical_speed) * vertical_speed * DRAG_COEFFICIENT * np.pi * PROPELLER_RADIUS**2
    drag_force = -drag_force_magnitude if vertical_speed > 0 else drag_force_magnitude

    gravity_force = PROPELLER_MASS * GRAVITY
    net_force = lift_force - gravity_force - drag_force

    # Update motion
    vertical_acceleration = net_force / PROPELLER_MASS
    vertical_speed += vertical_acceleration * TIME_STEP
    vertical_position += vertical_speed * TIME_STEP

    # Update rotation speed (simplified deceleration due to drag)
    rotation_deceleration = 0.1 * rotation_speed
    rotation_speed -= rotation_deceleration * TIME_STEP
    if rotation_speed < 0:
        rotation_speed = 0

    upward_force_values.append(lift_force - drag_force)
    downward_force_values.append(gravity_force)

    time += TIME_STEP


# Animation (No changes needed here for size or axes)
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
ax_propeller = axes[0, 0]
ax_position = axes[0, 1]
ax_forces = axes[1, 0]

# Propeller appearance (Radius is constant now)
propeller_stick, = ax_propeller.plot([0, 0], [-0.1, 0.1], color='black', linewidth=3)
propeller_patch = patches.Circle((0, 0), PROPELLER_RADIUS, facecolor='green', edgecolor='black')  # Radius is constant
ax_propeller.add_patch(propeller_patch)


force_text = ax_propeller.text(0.05, 0.9, "", transform=ax_propeller.transAxes)

ax_propeller.set_xlim(-0.2, 0.2)
ax_propeller.set_ylim(-0.5, 1)
ax_propeller.set_aspect('equal')

def init():
    propeller_stick.set_data([], [])
    propeller_patch.center = (0,0)
    return propeller_stick, propeller_patch,

def animate(i):
    x_center = 0
    y_center = position_values[i]

    # Propeller stick
    propeller_stick.set_data([x_center, x_center], [y_center - 0.1, y_center + 0.1])

    # Propeller rotation
    angle = rotation_angles[i]
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])

    rotated_circle = np.dot(rotation_matrix, np.array([PROPELLER_RADIUS, 0]))
    propeller_patch.center = (x_center + rotated_circle[0], y_center + rotated_circle[1])

    # Adjust axes dynamically
    y_min = min(min(position_values[:i+1]) - 0.2, -0.5)
    y_max = max(max(position_values[:i+1]) + 0.2, 1)
    ax_propeller.set_ylim(y_min, y_max)
    ax_propeller.set_xlim(-0.2, 0.2)

    up_force = upward_force_values[i]
    down_force = downward_force_values[i]

    force_color = "green" if up_force > down_force else "red"
    force_text.set_text(f"Upward Force: {up_force:.2f} N\nDownward Force: {down_force:.2f} N")
    force_text.set_color(force_color)

    return propeller_stick, propeller_patch,

ani = animation.FuncAnimation(fig, animate, frames=len(time_values), init_func=init, interval=20, blit=False, repeat=False)

# Position plot
ax_position.plot(time_values, position_values)
ax_position.set_xlabel("Time (s)")
ax_position.set_ylabel("Vertical Position (m)")
ax_position.set_title("Propeller Vertical Motion")
ax_position.grid()

# Forces plot
ax_forces.plot(time_values, upward_force_values, color='green', label='Upward Force')
ax_forces.plot(time_values, downward_force_values, color='red', label='Downward Force')
ax_forces.set_xlabel("Time (s)")
ax_forces.set_ylabel("Force (N)")
ax_forces.set_title("Forces on Propeller")
ax_forces.legend()
ax_forces.grid()

plt.tight_layout()
plt.show()