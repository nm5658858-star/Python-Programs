# 1. Zeros function creates an array (either one dimensional or multi dimensional) and fill all the values with zero (0)

import numpy as np
arr = np.zeros(5)
print(arr)

import numpy as np
arr = np.zeros((2,3))
print("Other method:")
print(arr)

# 2. Ones function creates an array (either one dimensional or multi dimensional) and fill all the values with one (1)

import numpy as np
arr = np.ones(5)
print(arr)

import numpy as np
arr = np.ones((2,3))
print("Other method:")
print(arr)

# 3. Eye creates an array with all the diagonal elements as 1 and rest as zero (in a square matrix).
# In case of a non square matrix the values are still one for diagonal (upto which it can draw diagonal) and rest are zero.

import numpy as np
arr = np.eye(3)
print("Eye function: ")
print(arr)

import numpy as np
arr = np.eye(3,4)
print("Other eye function")
print(arr)


# 4. Diag function creates a two dimensional array with all the diagonal elements as the given value and rest as zero in a square matrix.

import numpy as np
arr = np.diag([1,5,3,7])
print("diag function")
print(arr)

import numpy as np
arr = np.diag([1,5,3,7])
print("For only...",np.diag(arr))

# 5. randint function is used to generate a random number between a given range. Syntax: (min, max, total_values)

import numpy as np
arr  = np.random.randint(1,10,3)
print("randint function:",arr)    # Output can be any three number between 1 to 9

# 6. rand function is used to generate a values between 0 to 1. Syntax: (number of values)
import numpy as np
arr = np.random.rand(5)
print("rand function:",arr)     # Output can be any 5 numbers between 0 and 1

# 7. randn function is used to generate a random values close to zero. This may return positive or negative numbers as well.
# Syntax: rand.(number_of_values)
import numpy as np
arr = np.random.randn(5)
print("randn function:",arr)     # Output can be 5 numbers centered to zero



