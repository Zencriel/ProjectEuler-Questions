"""
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 5 squared is 25; it is also an odd square.
The first 5 square numbers are: 1, 4, 16, 25, 36, and the sum of the odd squares is 1 + 9 + 25 = 35.
Among the first 856 thousand square numbers, what is the sum of all the odd squares?
"""

#856/2 = 428 thousand odd squares.

def formula(numsquares):
    interimsum = numsquares*(((4)*(numsquares**2))-1)
    return interimsum/3

print(formula(428000))