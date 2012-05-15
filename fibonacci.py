#!/usr/bin/python
"""
As our program gets more complex, it makes sense to take certain parts and turn 
them into FUNCTIONS. Functions are like miniature programs inside your program. 
The program can CALL (i.e., start, invoke) a function, at which point it will 
do something and then RETURN (i.e., exit) to the main program. Your program can 
also pass PARAMETERS (data, variables, values, etc.) to the function if it will 
need to know more in order to complete its task.
"""

# Define a function (fib) which takes one parameter (t).
def fib(t):
  f0, f1 = 0, 1
  f = [ ]
  f.append(f0)
  f.append(f1)

  for i in range(2,t): # t represents the end of our range.
    fn = f1 + f0
    f.append(fn)
    f0 = f1
    f1 = fn
  
  print f

fib(12) # Call function fib and pass 12 as its parameter (so t = 12).

"""
Result: 
$ ~: fibonacci.py
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
"""