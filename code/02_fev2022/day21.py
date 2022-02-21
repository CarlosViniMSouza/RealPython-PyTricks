# collections.Counter lets you find the most common elements in an iterable:

import collections
col = collections.Counter('helloworld')

print(col)
# output: Counter({'l': 3, 'o': 2, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})

print(col.most_common(3))
# output: [('l', 3), ('o', 2), ('e', 1)]
