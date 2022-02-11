# converting information into various types

var = 5

# 1 - convert to string
var = str(var)
print(type(var))

# 2 - convert to float

var = float(var)
print(type(var))

# 3 - convert to integer again
var = int(var)
print(type(var))

# 4 - convert to list

var = list([var])
print(type(var))

# 5 - convert to tuple

var = tuple((var))
print(type(var))

"""
Output:

<class 'str'>
<class 'float'>
<class 'int'>
<class 'list'>
<class 'tuple'>
"""
