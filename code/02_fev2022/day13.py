# Python's list slice syntax can be used without indices for a few fun and useful things:

# You can clear all elements from a list:
lst = [1, 2, 3, 4, 5]
del lst[:]
print(lst)
# Output: []

# You can replace all elements of a list without creating a new list object:
a = lst
lst[:] = [7, 8, 9]

print(lst)
# Output: [7, 8, 9]

print(a)
# Output: [7, 8, 9]

print(a is lst)
# Output: True

# You can also create a (shallow) copy of a list:
b = lst[:]
print(b)
# Output: [7, 8, 9]

print(b is lst)
# Output: False
