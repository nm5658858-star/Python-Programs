print("Indexing in 1-D Array")
import numpy as np
a = []
size = int(input("Enter how many numbers: "))
for i in range(size):
    val = int(input("Enter number:"))
    a.append(val)
arr = np.array(a)
for i in range(arr.size):
    print(arr[i])
sum = 0
for i in range(arr.size):
    sum = sum + arr[i]
print("Sum of array elements =",sum)
    
# It supports indexing from left to right as well as right to left.
# When left to right, indexing starts from zero, while right to left, indexing starts from -1
# The indexing technique is similar to indexing technique of List.

print("Slicing in 1-D Array")
import numpy as np
a = []
size = int(input("Enter how many numbers: "))
for i in range(size):
    val = int(input("Enter number:"))
    a.append(val)
arr = np.array(a)
for i in range(arr.size):
    print(arr[i])
print("Full array is:",arr)
arr1 = arr[2:4]      # This will make a new array with element from array arr from index 2 to 3
print("Sliced array is:",arr1)
# The slicing technique is much similar to indexing technique of List.
