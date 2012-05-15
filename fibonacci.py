#!/usr/bin/python
"""
Python comes with a vast collection of built-in functions that are designed to 
make things easier for you. For example, len() will tell you how long something 
is. Let's use len() to make fib() simpler.
"""

# Define a function (fib) which takes one parameter (t).
def fib(t):
  f = [ 0, 1 ] # Create a list with our seed values already on it.

  # len(f) will find out how many items are on our list (f) and return the 
  # answer (in this case, 2). We can use the len() function to determine the 
  # start of our range automatically. This means that if you were to add 
  # another number to f at the start (such as 1, which is the next number in 
  # the Fibonacci sequence), the function would still work. 
  for i in range(len(f),t): 
    fn = f[len(f)-1] + f[len(f)-2]
    f.append(fn)
  
  print f

fib(12)

"""
Result: 
$ ~: fibonacci.py
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
"""