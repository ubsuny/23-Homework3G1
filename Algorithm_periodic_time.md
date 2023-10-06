# Periodic time calculation:
To calculate the periodic time, this formula will be used

$$
T=2*\pi * \sqrt(l/g)
$$

where l is the length of the string in meters, g is the acceleration due to gravity in $m/s^2$
## The Algorithm:
File(1): Algorithm.py
1- start with defining a function to calculate the periodic time ``` calculate_periodic_time(l) ```  with agrument l 

- variable g where g is constant of 9.81 m/s^2.

2- use lambda function to calculate the periodic time ``` lambda l: 2* math.pi/ math.sqrt(g / l) ```. 

3-   make the algorithm.py file callable module  ``` __all__=["calculate_periodic_time"] ```.

File (2): Period.py
 1- Create another python file and import the Module file containing the algorithm ``` import algorithm ```.
 
2- Ask the user to enter the lengths separated by commas and use them to create a list of floats and then print the inputs as a list of length.

```
lengths_list = input("Enter a list of length, separated by commas: ")
  
lengths_list = lengths_list.split(",")
 
integer_list = []
for element in lengths_list:
    integer_list.append(float(element))
print("your list of lengths is: ", integer_list,"meters")
   
```

3- use map function to allow calculation of time using each element of the list 
```  periodic_times = map(calculate_periodic_time(integer_list), integer_list) ```.

4- create a list of T: periodic times using the periodic_times map elements ```  T=[periodic_time for periodic_time in periodic_times] ```

5- round the elements of the times list to 2 sig figs ``` round_time=[round(element,2) for element in T]``` 
6- print results ``` print("periodic times corresporing to the lengths are ", round_time, "seconds")```



## python code:

# This is Python code
#File (1) Algorithm Module:

```

#algorithm.py
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
__all__=["calculate_periodic_time"]
```
# file (2): "Period.py" the code file with function imported from the algorithm module:
```
  #-----------------------------------------------------------#
#import the algorithm module:
import algorithm
#import the periodic time function feom the algorithm module
from algorithm import calculate_periodic_time
#ask the user to input list of lengths separated by commas
lengths_list = input("Enter a list of length, separated by commas: ")
  # Split the user input string into a list.
lengths_list = lengths_list.split(",")
  # Convert the elements of the list to floats
integer_list = []
for element in lengths_list:
    integer_list.append(float(element))
# Print the integer list.
print("your list of lengths is: ", integer_list,"meters")
    #--------------------------------------------------------------#
 # Use map to apply the lambda function to each length in the list
periodic_times = map(calculate_periodic_time(integer_list), integer_list)
# Print the periodic times and round them to 2 sig digits
T=[periodic_time for periodic_time in periodic_times]
round_time=[round(element,2) for element in T]
#Print the periodic times rounded and a msg to the user
print("periodic times corresporing to the lengths are ", round_time,"seconds")

```

#RESULT of RUNNING THe code:
<img width="825" alt="Screen Shot 2023-10-05 at 9 45 08 PM" src="https://github.com/ubsuny/23-Homework3G1/assets/38404107/806870ca-34bd-4fa7-9681-dff2699df368">


Resources: 
- [Python Lambda](https://www.w3schools.com/python/python_lambda.asp)
- [bard.google](https://bard.google.com/faq#coding)
- [Python_Map()](https://www.geeksforgeeks.org/python-map-function/)
- [Python map() – List Function with Examples](https://www.freecodecamp.org/news/python-map-explained-with-examples/)
