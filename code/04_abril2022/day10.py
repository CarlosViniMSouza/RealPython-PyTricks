# Python 3 allows unicode variable names:

import math

π = math.pi


class SpinalTap:
    pass


SpinalTap()
# output: <Spin̈alTap object at 0x10e58d908>

# Only letter-like characters work, however:

🍺 = "beer"

beer = 🍺

"""
output:

SyntaxError:
"invalid character in identifier"
"""
