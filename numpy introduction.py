# Numpy is a Python package which stands for "Numerical Python"
# It was created in 2005 by Travis Oliphant
# Using Numpy we can perform following functionalities:
# 1. Mathematical and logical operations on arrays.
# 2. Fourier transforms and routines for shape manipulation.
# 3. It has built in functions for Linear Algebra random number generations.
# 4. Used for scientific calculations.
# 5. It is faster than Python List.
# 6. It is fast because it is associated with C Programming.
# NUMPY is often called as an alternate for MatLab ( a programming platform,
# specifically for engineers and scientists for Data Analysis, Developing Algorithms,
# create models and applications etc).
# NUMPY is used with packages like SciPy (Scientific Python).
# and Mat-Plotib (Plotting library) and this makes it capable to replace MATLAB.
# Dimensional Array is referred to as Vectors, Matrix and Tensor.

import numpy as np

# Create a simple array
arr = np.array([[10, 20, 30, 40, 50],[60,70,80,90,100]])
print("NumPy Array:", arr)

# Print basic properties
print("Shape:", arr.shape)
print("Data type:", arr.dtype)

