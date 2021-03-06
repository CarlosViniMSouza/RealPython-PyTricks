# Python's list comprehensions are awesome.

"""
vals = [expression
        for value in collection
        if condition]

# This is equivalent to:

vals = []
for value in collection:
    if condition:
        vals.append(expression)
"""

# Example:

even_squares = [x * x for x in range(10) if not x % 2]
print(even_squares)

# Output: [0, 4, 16, 36, 64]