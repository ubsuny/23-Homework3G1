import math

# Define the frequency (in Hz) and amplitude of the sine wave
frequency = 2  # Hz
amplitude = 1.0

# Create a lambda function for the periodic time function
periodic_function = lambda t: amplitude * math.sin(2 * math.pi * frequency * t)

# Generate and print values of the periodic function at different time points
time_points = [0.0, 0.25, 0.5, 0.75, 1.0]

for t in time_points:
    value = periodic_function(t)
    print(f"At t = {t}, value = {value}")

At t = 0.0, value = 0.0
At t = 0.25, value = 1.2246467991473532e-16
At t = 0.5, value = -2.4492935982947064e-16
At t = 0.75, value = 3.6739403974420594e-16
At t = 1.0, value = -4.898587196589413e-16

