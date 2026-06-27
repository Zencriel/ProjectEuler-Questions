"""
By considering the terms in the Fibonacci sequence
whose values do not exceed four million, find the sum of the even-valued terms.
"""

memo = {0: 0, 1: 1}


def fibonacci_number(n):
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_number(n - 1) + fibonacci_number(n - 2)
    return memo[n]

correct_numbers = [fibonacci_number(i) for i in range (0,34) if fibonacci_number(i) < 4000000 and fibonacci_number(i) % 2 ==0 ]
total = sum(correct_numbers)
print(total)

