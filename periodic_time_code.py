
import math

def calculate_periodic_time(l):
  """Calculates the periodic time of a simple pendulum.

  Args:
    l: The length of the pendulum in meters.

  Returns:
    The periodic time of the pendulum in seconds.
  """
# Acceleration due to gravity in meters per second squared.
  g = 9.81  
# use lambda function calculate the periodic time where l is the length of the string and return the value calculated
  calculate_periodic_time= (lambda l: 2* math.pi/ math.sqrt(g / l))
  return calculate_periodic_time

# Define a list of lengths of pendulums
x = [0.5, 1, 1.5, 2, 2.5]

# Use map to apply the lambda function to each length in the list
periodic_times = map(calculate_periodic_time(x), x)

# Print the periodic times and round them to 2 sig digits

T=[periodic_time for periodic_time in periodic_times]
print("\n","periodic time for l= ", x[0] , "m is ", round(T[0],ndigits=2),"seconds", "\n", "periodic time for l= ", x[1] , "m is ", round(T[1],ndigits=2),"seconds","\n", "periodic time for l= ", x[2] , "m is ", round(T[2],ndigits=2), "seconds", "\n", "periodic time for l= ", x[3] , "m is ", round(T[3],ndigits=2),"seconds","\n", "periodic time for l= ", x[4] , "m is ", round(T[4],ndigits=2),"seconds",)
