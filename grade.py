"""
EXERCISE 01 - Grade calculator
Topic: if / elif / else

TASK
----
Given a marks value, print the grade using this scale:
    90 and above  -> A
    75 to 89      -> B
    60 to 74      -> C
    40 to 59      -> D
    below 40      -> F

Then test it with several different marks values.

EXPECTED OUTPUT (for the values already listed below)
----------------------------------------------------
95 -> A
82 -> B
72 -> C
55 -> D
30 -> F
"""

    # TODO: replace this with an if / elif / else chain that returns
    #       "A", "B", "C", "D" or "F" based on the scale above.
    #       Remember: test the STRICTEST condition first.

def grade_for(marks):
    if marks>=90:
        return "A"
    elif marks>=75 and marks<=89:
        return "B"
    elif marks>=60 and marks<=74:
        return "C"
    elif marks>=40 and marks<=59:
        return "D"
    else:
        return "F"

for m in [95, 82, 72, 55, 30]:
    print(m, "->", grade_for(m))