#!/usr/bin/python
"""
Our previous example prints each value out on a separate line, but it'll be a 
lot easier to read if we just print them all out at the end, as one big list. 
Assigning a variable with square brackets around its value(s) creates a LIST. 
You can also create an empty list by putting nothing between the brackets.
"""

f0, f1 = 0, 1 

f = [ ] # Create an empty list.
f.append(f0) # Put our seed values on the list at the end.
f.append(f1)

for i in range(2,12): 
  fn = f1 + f0
  f.append(fn)
  f0 = f1
  f1 = fn

# Print out the entire list.
print f

"""
Result: 
$ ~: fibonacci.py
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
"""
