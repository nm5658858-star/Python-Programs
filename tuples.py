# Tuple is a collection which is ordered and unchangeable.
# In Python, tuples are written with round brackets.
# Tuples in Python are very similar to list which contains different types of elements.
# 1. The list is created using [] brackets and tuples are created using () brackets.
# tuple_difference1  = (1,2,3,"Saif","Malik")
# list_difference1 = [1,2,3,"Saif","Malik"]

# 2. The list is mutable(changeable) whereas the tuples are immutable(unchangeable)
# listdiff2 = [1,2,3,"Saif","Malik"]
# listdiff2 [2] = 10 ----> print(a) -----> OUTPUT: 1,2,10,Saif,Malik (2 <==> 10)

# tupledif2 = (1,2,3,"Saif","Malik")
# tupledif2 [2] = 10 ----> print(a) -----> OUTPUT: Error (tuple is immutable)

# 3. List occupies more memory space as compared that tuples.
print("Demo program to figure out MEMORY comparison of list and tuple")
import sys
list1 = [1,2,3,"Saif",True,"Malik"]
tuple1 = (1,2,3,"Saif",True,"Malik")
print("Size of list: ",sys.getsizeof(list1))         # size = 104
print("Size of tuple: ",sys.getsizeof(tuple1))   # size = 88

# 4. List takes more time to execute as compared to tuples.
# print("Demo program to figure out TIME comparison of list and tuple")
# import timeit
# listtime = timeit.timeit(stmt = "[1,2,3,4,5,6,7,8,9]", number = 1000000)
# tupletime = timeit.timeit(stmt = "(1,2,3,4,5,6,7,8,9)", number = 1000000)
# print("List takes time: ",listtime,"s")
# print("Tuple takes time: ",tupletime,"s")
