#!/usr/bin/python
"""
In order to print a Fibonacci sequence, we need to tell Python what to do. 

With just a few commands, Python will print out the first twelve Fibonacci 
numbers for us.

Note: Any text appearing between triple quotes (like this block of text) is a 
BLOCK COMMENT, while any text that appears between a pound sign (#) and the end 
of the line is an INLINE COMMENT. Python will ignore them.
"""

# Set our seed values of 0 and 1.
f0, f1 = 0, 1 

# Since f0 and f1 are the first two numbers in out sequence, 
# let's print them out. Two down, ten to go!
print f0
print f1

# This is a FOR LOOP, which will repeat as long as its condition (i) is true. 
# Each time we reach the end of the loop, i is incremented. When the condition 
# is no longer true (i.e., when i is not in the range specified), we exit the 
# loop. (Note: our range starts at 2, because we already printed the first two 
# numbers above.
for i in range(2,12): 
  fn = f1 + f0 # Here's our Fibonacci formula.
  print fn
  f0 = f1 # Set f0 to be whatever f1 is. (f1 is not changed.)
  f1 = fn

"""
Result:
$ ~: fib.py
0
1
1
2
3
5
8
13
21
34
55
89
"""
