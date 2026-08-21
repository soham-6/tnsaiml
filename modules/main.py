"""
EXERCISE 10a - Your own module
Topic: writing a module + if _name_ == "_main_"

This file is a MODULE. Another file will import it.

TASK
----
1. Complete the three functions below.
2. Add the _name_ guard at the bottom so the demo prints ONLY when you
   run this file directly - not when main.py imports it.

Then run BOTH of these in the terminal and compare the output:
    python mathutils.py
    python main.py

PI = 3.14159
"""

import mathutils as m
import listconversion as l

# print(f"Perimeter of rectangle is {m.perimeter_rectangle()}")
# print(f"Area of circle is {m.area_circle()}")

conversion = l.list_conversion()
print(conversion)