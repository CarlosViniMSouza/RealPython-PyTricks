# The "timeit" module lets you measure the execution
# time of small bits of Python code

import timeit

t1 = timeit.timeit('"-".join(str(n) for n in range(100))',
                   number=10000)

print(t1)

# Output: 0.14173659999505617

t2 = timeit.timeit('"-".join([str(n) for n in range(100)])',
                   number=10000)

print(t2)

# Output: 0.11493170000903774

t3 = timeit.timeit('"-".join(map(str, range(100)))',
                   number=10000)

print(t3)

# Output: 0.1230548000021372
