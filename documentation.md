# To find the time period of simple pendulum
Simple Pendulum is a small bob of mass m, also known as pendulum bob which is suspended from
a light wire or string. The period of pendulum is the time required for pendulum to complete one oscillation. One oscillation is the motion of the pendulum beginning at some reference point and continuing untill the reference point is reached again. The time period (T) is estimated using: 

<img width="133" alt="Time_period" src="https://github.com/pratibha77118/23-Homework3G1/assets/72980895/4f12ecd9-c864-4d24-bc50-f1ad69072843">


L is the length of the string and g is acceleration due to gravity
# Objectives
1 To use a classical mechanics function as a python function and using this function as an argument in another function.
# Steps to implement
- Define a classical mechanics function as periodic time with arguments l and g. 
- Use Lambda function to calculate the periodic time.
- Save the file as a module
- Import module defined earlier.
- List the length values.
- Use map function to calculate time using each element in the lists.
- Create a list of periodic times using the map elements.
- Print results which takes the periodic time of index 0 in the length list and give its 
   corresponding value in the time lists.
- The process is repeated
  # Functions used
- Lambda Function : Lambda function is used as a substitute for fully fledge name function to use it as a simple operation. They have limitations in comparision to function defined by 'def'. They are mostly used for simple one linear operations and are not preferred for multisteps complex operations
- Map function: Map function is used to apply a specific function to each item in an iterable and return a new iterable containing the results.

# Code Using Module
Module is a file containing python definition and statements and can be imported into other modules. Using module we can import the file created earlier to use it in several programs. The filename is the module name with .py appended and is imported with the module name to run the program we want.
 ```python
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
```python
%%writefile algorithm.py
```
```python
import algorithm
lengths_list = input("Enter a list of length, separated by commas: ")
 # Split the user input string into a list.
lengths_list = lengths_list.split(",")
# Convert the elements of the list to integers
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
print("periodic times corresporing to the lengths are ", round_time,"seconds")

__all__=["period"]
    
```
# Output
<img width="524" alt="Output" src="https://github.com/pratibha77118/23-Homework3G1/assets/72980895/c2cb28a9-ffad-4d8a-82ca-d70922a0fb08">

#Unit_Test..
A unit test was done for this algorithm and was checked whethere the code works well or not. The unit test code can be seen below,  
import unittest
import math

# Define the function to calculate the periodic time
def calculate_periodic_time(l):
    """Calculates the periodic time of a simple pendulum.

    Args:
        l: The length of the pendulum in meters.

    Returns:
        The periodic time of the pendulum in seconds.
    """
    # Acceleration due to gravity in meters per second squared.
    g = 9.81
    
    # Calculate the periodic time using the formula
    periodic_time = 2 * math.pi * math.sqrt(l / g)
    
    return periodic_time

class TestCalculatePeriodicTime(unittest.TestCase):

    def test_calculate_periodic_time(self):
        # Test cases with known results 
        **#BTW, these values are not correct, these are updated in the new file to merged as unit_test.** 
        test_cases = [
            (0.5, 2.007),  # (length, expected_periodic_time)
            (1.0, 4.498),
            (1.5, 6.283),
            (2.0, 8.987),
            (2.5, 11.178)
        ]

        # Perform the tests
        for length, expected_periodic_time in test_cases:
            result = calculate_periodic_time(length)
            assert math.isclose(result, expected_periodic_time, rel_tol=0.001)

if __name__ == '__main__':
    unittest.main()
It was found that, the unit test code has some environment compatibilty issues. The resul I got was, 
E
======================================================================
ERROR: /root/ (unittest.loader._FailedTest)
----------------------------------------------------------------------
AttributeError: module '__main__' has no attribute '/root/'

----------------------------------------------------------------------
Ran 1 test in 0.004s

FAILED (errors=1)
An exception has occurred, use %tb to see the full traceback.

SystemExit: True
/usr/local/lib/python3.10/dist-packages/IPython/core/interactiveshell.py:3561: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.
  warn("To exit: use 'exit', 'quit', or Ctrl-D.", stacklevel=1)
But the Ran 1 test in 0.004s can bee seen here. after trying fixing the code, I found a solution to avoid the issue, by adding the extra line to the code,[\ref] 
#unittest.main(argv=['first-arg-is-ignored'], exit=False)
_**And The reason is that unittest.main looks at sys.argv and first parameter is what started IPython or Jupyter, therefore the error about kernel connection file not being a valid attribute. Passing explicit list to unittest.main will prevent IPython and Jupyter look at sys.argv. Passing exit=Fals will prevent unittest.main to shutdown the kernell process_**
By doing this, the unit test code unifortunatly failes the actual code. Which seems very unlikely. 



# Implementing Pylint
Pylint is a powerful tool that help to maintain quality and consistency of python codes. It helps to write cleaner, more readable, and less error-prone code by identifying and flagging potential issues and errors adherence to coding standards.

[algorithm10_pylint](https://colab.research.google.com/drive/1SJCVF3-9tEVC18AI5cqoRusr9Ej-bVkn?usp=sharing)
<img width="848" alt="Pylint10" src="https://github.com/pratibha77118/23-Homework3G1/assets/72980895/0a15f645-3d50-4dc0-866e-753f1b7aa71e">

# Using Assert function
Assert is a build in python function used for debugging purposes and check the given condition. If the given condition is true then the program continues to run as normal but if the condition is false then assert raises an 'AssertionError' with a error message which helps for debugging.
# Sources
- [\ref] https://medium.com/@vladbezden/using-python-unittest-in-ipython-or-jupyter-732448724e31
- (https://openai.com/chatgpt)
- (https://docs.python.org/3/tutorial/modules.html)
- (https://pypi.org/project/pylint/)
- [Python Lambda](https://www.w3schools.com/python/python_lambda.asp)
- [bard.google](https://bard.google.com/faq#coding)




  

