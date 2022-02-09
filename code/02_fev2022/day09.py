# Python 3.5+ supports 'type annotations' that can be used with tools like Mypy to write statically typed Python:

def my_add(a: int, b: int) -> int:
    return a + b


print(my_add(3, 5))
# Output: 8

print(type(my_add))
# Output: <class 'function'>
