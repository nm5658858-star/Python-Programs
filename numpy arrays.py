# # 1-D ARRAYS
# import numpy as np
# a = [1,2,3,4,5]
# myarr = np.array(a)
# # myarr = np.array([1,2,3,4,5])      # same as upper line
# print(myarr)
# 
# 
# import numpy as np
# a = []
# n = int(input("Enter size of array:"))
# for i in range(n):
#     val = int(input("Enter number:"))
#     a.append(val)
# myarray = np.array(a)
# print(myarray)

# 2-D ARRAYS
import numpy as np
a = [[1,2,3],[4,5,6],[7,8,9]]
myarr = np.array(a)
print("2-D Array",myarr)
print()
print("2d array by other method")
myarr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(myarr)
print("Total Dimensions: ",myarr.ndim)
print("Total Shapes: ",myarr.shape)
