print("Traversing Tuple")
tuple1 = (1,2,3,4)
for i in tuple1:
    print(i)

tup1 = (1,2,3,4)
for i in range(len(tup1)):    # len = 4-1 = 3
    print(tup1[i])    #tup[1] = 2

print("Joining Tuple")
t1 = (1,2,3,4,5)
t2 = (6,7,8)
t3 = t1 + t2
print("t1 is:",t1," and t2 is:",t2," and Joined tuples: ",t3)

# print("Repeating or Replicating Tuples")
# tp1 = (1,2,3)
# tp2 = tp1*3
# print("Repeating tuples: ",tp2)
# 
print("Slicing the Tuples")
tuple1 = (1,2,3,4,5)
tuple2 = tuple1[3:5:1]
print("After Slicing: ",tuple2)

t1 = (10,11,12,13,14)
t2 = t1[0:5:2]
print("With step value: ",t2)
