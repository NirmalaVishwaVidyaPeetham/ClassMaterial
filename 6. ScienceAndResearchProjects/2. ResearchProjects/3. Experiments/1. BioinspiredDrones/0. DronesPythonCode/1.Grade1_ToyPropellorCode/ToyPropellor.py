## Drag force equations etc. may or may not be correct. Overall the code shows how the toy propellor goes up or down.


#Create a python model of a toy propellor. As the propellor is given an initial rotation,
# the air pushes it upwards, while gravity pulls it downwards.
# If the initial speed of rotation is greater than some value (beyond the force due to gravity),
 # then it will go up. Gradually as the propellor slows down,
# it starts coming back down.
# Show the rotation of the propellor and it's vertical motion. At each point of time,
# also the values for upwards force and downwards force - Show these values in green
# if upwards > downwards, in red if upwards < downwards.

# Based on reference:
# https://scholarlycommons.pacific.edu/cgi/viewcontent.cgi?article=1086&context=soecs-facarticles

# TODO:
# 1. Bug fix needed: the total time is changing based on simulation time.
# 2. Check about drag_force, and its usage.. does it depend of vertical velocity? How does it affect motion?
# 3. Check about rotation deceleration

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

BASE_VERTICAL_POSITION = 0.0  # meters
TORQUE_COEFFICIENT = 0.006

#PLOT CONSTANTS
PLT_AXIS_BUFFER=0.5

# Simulation parameters
TIME_STEP = 0.02
SIMULATOR_DURATION = 100

#Total spin time is updated later
SPIN_DURATION=None

######  -- Propeller properties start from here.. These values can be changed ----
# Constants
GRAVITY = 9.8 #meter/sec^2
AIR_DENSITY = 1.225 #kg/meter^3 #TODO in reference, this value is provided as 1; AI: 1.225
LIFT_COEFFICIENT = 0.8 #TODO in reference, this value is provided as 1; AI: 0.8
DRAG_COEFFICIENT = 0.5

# PROPELLER PROPERTIES
PROPELLER_FANBLADE_LENGTH = 0.1  #in meters #TODO CHANGED FROM 0.05
PROPELLER_FANBLADE_WIDTH = 0.02  #in meters
PROPELLER_STICK_DIAMETER = 0.005  #in meters

# Intial conditions
INITIAL_VERTICAL_SPEED = 0.0

# Propeller blade properties -- Dont change this
# there is no clear equation to show relationship of fan speed vs num of blades
# Without that, it does not make a difference. Since this is based on the reference with two blades,
# keeping it as a constant for this simulation.
# Reference: https://scholarlycommons.pacific.edu/cgi/viewcontent.cgi?article=1086&context=soecs-facarticles
# num_blades = 2
#blade_length = PROPELLER_RADIUS * 0.8
#PROPELLER_MASS_PER_BLADE = 0.0035 # per blade in kg
#PROPELLER_MASS = num_blades * PROPELLER_MASS_PER_BLADE

######  -- CODE STARTS -- DO NOT CHANGE FROM HERE ----

# Lists to store data for plotting
time_values = []
position_values = []
rotation_angles = []
upward_force_values = []
downward_force_values = []
vertical_speed_values = []
forces_balance_index=None

def compute_propellor_trajectory(propeller_mass = 0.007, starting_rotation_speed = 133.0, starting_fan_release_height = 5.0):
    # Initialize variables
    rotation_speed = starting_rotation_speed
    vertical_position = starting_fan_release_height
    vertical_speed = INITIAL_VERTICAL_SPEED
    initial_lift_force = 0  # Store the initial lift force
    gravity_force = propeller_mass * GRAVITY
    # Simulation loop
    global forces_balance_index
    time = 0
    while time <= SIMULATOR_DURATION and vertical_position > BASE_VERTICAL_POSITION:
        time_values.append(time)
        position_values.append(vertical_position)
        rotation_angle = (rotation_speed * time) % (2 * np.pi)
        rotation_angles.append(rotation_angle)


        # Calculate forces (Lift force now only decreases)
        # https://scholarlycommons.pacific.edu/cgi/viewcontent.cgi?article=1086&context=soecs-facarticles
        #Formula lift_force = 0.5 * LIFT_COEFFICIENT * AIR_DENSITY * planform_area * speed
        num_blades = 2
        planform_area = num_blades * PROPELLER_FANBLADE_LENGTH * PROPELLER_FANBLADE_WIDTH   # for propeller with num_blades
        average_propeller_speed = rotation_speed * PROPELLER_FANBLADE_LENGTH * 0.5  # omega*r/2

        lift_force = 0.5 * AIR_DENSITY * LIFT_COEFFICIENT * planform_area * average_propeller_speed**2

        if time == 0:  # Store initial lift
            initial_lift_force = lift_force

        lift_force = min(lift_force, initial_lift_force) # Lift can only decrease
        #Drag force equation: https://www.grc.nasa.gov/www/k-12/VirtualAero/BottleRocket/airplane/drageq.html
        drag_force_magnitude = 0.5 * AIR_DENSITY * (vertical_speed**2) * DRAG_COEFFICIENT * planform_area

        # upward_force = lift_force if vertical_speed > 0 else lift_force+drag_force_magnitude
        # downward_force = gravity_force + drag_force_magnitude if vertical_speed > 0 else gravity_force

        upward_force = lift_force
        downward_force = gravity_force + drag_force_magnitude

        net_force = upward_force-downward_force

        upward_force_values.append(upward_force)
        downward_force_values.append(downward_force)

        if upward_force <= downward_force and forces_balance_index == None:
            forces_balance_index = len(downward_force_values)

        # print(f'lift: {lift_force} ; drag: {abs(drag_force)} ; gravity: {gravity_force} ; net_force: {net_force}')
        # print(f'rotation_speed: ({(rotation_speed)})')

        # Update motion
        vertical_acceleration = net_force / propeller_mass
        vertical_speed = vertical_speed + vertical_acceleration * TIME_STEP
        vertical_position = vertical_position + vertical_speed * TIME_STEP
        vertical_speed_values.append(vertical_speed)

        # Update rotation speed (simplified deceleration due to drag)
        # https://aviation.stackexchange.com/questions/105788/propeller-torque-calculation
        # drag_rotation_torque = TORQUE_COEFFICIENT * AIR_DENSITY * rotation_speed**2 * (2*PROPELLER_FANBLADE_LENGTH)**5

        # FROM AI:  searched for "rotational deceleration formula for propeller two blade"
        # The rotational deceleration formula for a propeller, including a two-blade propeller, can be expressed as: α = (T_brake - T_drag) / (I_propeller * ω), where:
        # α: is the angular deceleration (radians per second squared)
        # T_brake: is the braking torque applied to the propeller
        # T_drag: is the aerodynamic drag torque acting on the propeller
        # I_propeller: is the moment of inertia of the propeller
        # ω: is the angular velocity of the propeller (radians per second)
        # Key points to remember:
        # Moment of inertia (I_propeller):
        # This value depends on the mass distribution of the propeller blades and can be calculated using the formula: I = ∫(r^2 * dm), where "r" is the distance from the axis of rotation to a small mass element "dm".
        # Drag torque (T_drag):
        # This torque is caused by air resistance acting on the rotating propeller blades and is typically a function of the propeller's geometry, air density, and rotational speed.
        # Braking torque (T_brake):
        # This is the external torque applied to slow down the propeller, which could be from a motor control system or a brake mechanism.

        # rotation_moment_of_interia = PROPELLER_MASS*(PROPELLER_FANBLADE_LENGTH)**2
        # rotation_deceleration = drag_rotation_torque/(rotation_moment_of_interia*rotation_speed)
        # print('rotation_deceleration:', rotation_deceleration)

        rotation_deceleration = 0.1 * rotation_speed

        rotation_speed =rotation_speed - rotation_deceleration * TIME_STEP
        if rotation_speed < 0:
            rotation_speed = 0

        time += TIME_STEP
        #print("Vertical acc, speed, position: ", vertical_acceleration, vertical_speed, vertical_position)

    if vertical_position < BASE_VERTICAL_POSITION:
        position_values.append(BASE_VERTICAL_POSITION)
        time_values.append(time)
        rotation_angles.append(rotation_angle)
        upward_force_values.append(upward_force)
        downward_force_values.append(downward_force)
        vertical_speed_values.append(vertical_speed)


    global SPIN_DURATION
    # TODO: This is changing based on TIME_STEP -- Need to fix the below line
    # SPIN_DURATION = (2*np.pi/rotation_speed)*((max(position_values)-BASE_VERTICAL_POSITION)/PROPELLER_STICK_DIAMETER)
    SPIN_DURATION = max(time_values)

    print(f'forces_balance_index: {forces_balance_index}')
    print(f'Number of timesteps: len({len(time_values)})')
    print(f'\nFlight_duration: {SPIN_DURATION:.2f} time steps')

    for indx in range(1, len(vertical_speed_values)):
        if np.sign(vertical_speed_values[indx-1]) * np.sign(vertical_speed_values[indx]) < 0:
            print(f"Velocity direction changes at : {time_values[indx-1]:.2f} time steps")

    _plot_propellor_trajectory(propeller_mass, starting_rotation_speed, starting_fan_release_height)

    return
def _plot_propellor_trajectory(propeller_mass, starting_rotation_speed, starting_fan_release_height):
    # Animation (No changes needed here for size or axes)

    fig = plt.figure(figsize=(12, 8))
    num_cols=3
    num_rows=4
    spec = mpl.gridspec.GridSpec(ncols=num_cols, nrows=num_rows)

    ax_propeller = fig.add_subplot(spec[0:,:num_cols-1])
    ax_position = fig.add_subplot(spec[0,num_cols-1])
    ax_forces = fig.add_subplot(spec[1,num_cols-1])
    ax_velocity = fig.add_subplot(spec[2,num_cols-1])
    ax_propeller_properties = fig.add_subplot(spec[3,num_cols-1])

    # Propeller and stick properties
    propeller_plt_fan_diameter = min(2*PROPELLER_FANBLADE_LENGTH * 50, 5)
    propeller_plt_fan_width = min(PROPELLER_FANBLADE_WIDTH*100, 5)
    stick_length = propeller_plt_fan_diameter*1
    stick_width = max(0.2, stick_length/100)
    rotation_center = (0, 0)

    # Propeller appearance (Radius is constant now)
    propeller_blade_line, = ax_propeller.plot([], [], lw=propeller_plt_fan_width, color='blue')
    propellor_stick = plt.Polygon([rotation_center], facecolor='brown', edgecolor='black')

    ax_propeller.add_patch(propellor_stick)
    force_text = ax_propeller.text(-0.6, 0.5, "", transform=ax_propeller.transAxes)

    # Propeller settings display
    propeller_initial_state_data = {
        '\nStarting conditions': '\n',
        'propeller_mass': propeller_mass,
        'starting_rotation_speed': starting_rotation_speed,
        'starting_fan_release_height': starting_fan_release_height,
        '\nOutput:\nTotal flight duration': np.round(SPIN_DURATION,3),
        'Maximum vertical height reached': np.round(max(position_values),3)
    }
    lines = [f'{key} : {value}' for key, value in propeller_initial_state_data.items()]
    ax_propeller_properties.text(0,1.1, '\n'.join(lines), ha='left', va='top', fontsize=10)
    ax_propeller_properties.axis('off')

    # Propeller plot
    ax_propeller.set_xlim(-propeller_plt_fan_diameter*0.7, propeller_plt_fan_diameter*0.7)
    ax_propeller.set_ylim( 0, max(position_values)+stick_length+propeller_plt_fan_diameter)
    ax_propeller.set_aspect('equal')

    # Position plot
    ax_position.set_xlabel("Time (s)")
    ax_position.set_ylabel("Vertical Position (m)")
    ax_position.set_title("Propeller Vertical Motion")
    ax_position.grid()

    # Forces plot
    ax_forces.set_xlabel("Time ")
    ax_forces.set_ylabel("Force (N)")
    ax_forces.set_title("Forces on Propeller")
    ax_forces.grid()

    #velocity plot
    ax_velocity.set_xlabel("Time")
    ax_velocity.set_ylabel("Vertical Velocity (m/s)")
    ax_velocity.set_title("Propeller Vertical Velocity")
    ax_velocity.grid()

    def init():
        propeller_blade_line.set_data([], [])
        propellor_stick.set_xy([rotation_center])
        return propeller_blade_line, propellor_stick,

    def animate(i):
        x_center = rotation_center[0]
        y_center = position_values[i]
        angle = rotation_angles[i]
        #spin_time_values = np.asarray(time_values)* SPIN_DURATION/max(time_values)
        spin_time_values = np.asarray(time_values)

        # Propeller blade coordinates
        propeller_x = [
            x_center - propeller_plt_fan_diameter / 2 * np.cos(angle),
            x_center + propeller_plt_fan_diameter / 2 * np.cos(angle),
        ]
        propeller_y = [
            y_center + stick_length - propeller_plt_fan_diameter / 2 * np.sin(angle),
            y_center + stick_length + propeller_plt_fan_diameter / 2 * np.sin(angle),
        ]

        # Propeller rotation
        propeller_blade_line.set_data(propeller_x, propeller_y)

        # Propeller stick coordinates
        stick_xy=[
            (x_center-stick_width/2., y_center),
            (x_center+stick_width/2., y_center),
            (x_center+stick_width/2., y_center + stick_length),
            (x_center-stick_width/2., y_center + stick_length),
        ]
        propellor_stick.set_xy(stick_xy)

        up_force = upward_force_values[i]
        down_force = downward_force_values[i]

        force_color = "green" if up_force > down_force else "red"
        force_text.set_text(f"Forces:\nUpward: {up_force:.2f} N\nDownward: {down_force:.2f} N")
        force_text.set_color(force_color)

        #update forces plot
        ax_forces.plot(spin_time_values[:i], upward_force_values[:i], color='green', label='Upward Force')
        ax_forces.plot(spin_time_values[:i], downward_force_values[:i], color='red', label='Downward Force')
        ax_forces.set_ylim(min(upward_force_values+downward_force_values)-PLT_AXIS_BUFFER/100,
                           max(upward_force_values+downward_force_values)+PLT_AXIS_BUFFER/100)
        ax_forces.set_xlim(-PLT_AXIS_BUFFER, max(spin_time_values)+PLT_AXIS_BUFFER)
        if i==0:
            ax_forces.legend(loc="upper left")

        # update position plot
        #max_position_index = position_values.index(max(position_values))
        color_change_index = forces_balance_index # = max_position_index
        ax_position.set_ylim(min(position_values), max(position_values)+PLT_AXIS_BUFFER)
        ax_position.set_xlim(-PLT_AXIS_BUFFER, max(spin_time_values)+PLT_AXIS_BUFFER)
        if i > color_change_index:
            ax_position.plot(spin_time_values[:color_change_index+1], position_values[:color_change_index+1], color='green', label='Positive')
            ax_position.plot(spin_time_values[color_change_index:i], position_values[color_change_index:i], color='red', label='Negative')
        else:
            ax_position.plot(spin_time_values[:i], position_values[:i], color='green')

        # update velocity plot
        ax_velocity.set_ylim(min(vertical_speed_values)-PLT_AXIS_BUFFER, max(vertical_speed_values)+PLT_AXIS_BUFFER)
        ax_velocity.set_xlim(-PLT_AXIS_BUFFER, max(spin_time_values)+PLT_AXIS_BUFFER)
        if i > color_change_index:
            ax_velocity.plot(spin_time_values[:color_change_index+1], vertical_speed_values[:color_change_index+1], color='green', label='Positive')
            ax_velocity.plot(spin_time_values[color_change_index:i], vertical_speed_values[color_change_index:i], color='red', label='Negative')
        else:
            ax_velocity.plot(spin_time_values[:i], vertical_speed_values[:i], color='green')

        return propeller_blade_line, propellor_stick,

    ani = animation.FuncAnimation(fig, animate, frames=len(time_values), init_func=init, interval=20, blit=False, repeat=False)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    compute_propellor_trajectory(propeller_mass = 0.007, starting_rotation_speed=133, starting_fan_release_height=5)
