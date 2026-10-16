# run each function call separately commenting the rest of the calls, otherwise it's causing some issues

from ToyPropellor import compute_propellor_trajectory

#compute_propellor_trajectory(propeller_mass = 0.007, starting_rotation_speed=133, starting_fan_release_height=5)
# Fan went a little bit up to 6.962m and fell down – fell after 4.12 seconds

#compute_propellor_trajectory(propeller_mass = 0.004, starting_rotation_speed=133, starting_fan_release_height=5)
# Decreased mass to 0.004 kg
# Fan went a bit up to 21.283m and fell down – fell after 6.98 seconds
# When mass decreased, height increased and total time increased

#compute_propellor_trajectory(propeller_mass = 0.117, starting_rotation_speed=133, starting_fan_release_height=5)
# Increased mass to 0.117 kg
# Fan did not go up and fell down from 5m – fell after 1.04 seconds
# When mass increased, height decreased and total time decreased

#compute_propellor_trajectory(propeller_mass = 0.007, starting_rotation_speed=200, starting_fan_release_height=5)
# Increased starting rotation speed to 200
# Fan went a bit up to 39.218m and fell down – fell after 8.9 seconds
# When starting rotation speed increased, height increased and total time increased

#compute_propellor_trajectory(propeller_mass = 0.007, starting_rotation_speed=100.66, starting_fan_release_height=5)
# Decreased starting rotation speed to 100.66
# Fan did not go up and fell down from 5m – fell after 1.5 seconds
# When starting rotation speed decreased, height decreased and total time decreased

# compute_propellor_trajectory(propeller_mass = 0.007, starting_rotation_speed=133, starting_fan_release_height=7)
# Increased fan release height to 7m
# Fan went a bit up to 8.972m and fell down – fell after 4.24 seconds
# When fan release height increased, height increased and total time increased

compute_propellor_trajectory(propeller_mass = 0.007, starting_rotation_speed=100.66, starting_fan_release_height=3)
# Decreased fan release height to 3m and rotation speed to 100.66
# Fan did not go up and fell down from 3m – fell after 1.26 seconds
# When fan release height decreased, height decreased and total time decreased
