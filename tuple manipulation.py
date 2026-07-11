print("Change Tuple Values...")
# Once a tuple is created, you cannot change its values because tuples are
# unchangeable or immutable.
# But there is another way to achieve this. You can convert the tuple into
# a list, and convert the list back into a tuple.
print("Example: 1")
x = ("apple","banana","mango")
y = list(x)
y[1] = "grapes"
x = tuple(y)
print(x)

print("Example: 2 -->Check if item exists:  Use of 'in' keyword")
tuple1 = ("Saif","Malik","Hamza","Rana")
if "Malik" in tuple1:
    print("Malik is present in tuple!")
else:
    print("Malik is not present in the tuple!")


# Once a tuple is created, you can't add items to it. Tuples are unchangeable
# t1 = ("apple","banana","cherry")
# t1[3] = "orange"  #==> error
# print(t1)
print("Example: 3 --> Conversion of tuple into list")
t1 = ("Islamabad","Lahore","Karachi","Peshawar","Quetta","Multan")
t2 = list(t1)
t2[2] = "Faisalabad"
t2.append("Karachi")
t1 = tuple(t2)
print(t1)

print("Example: 4 --' Use of 'del' statement")
tup1 = ("Ali","Ahmed","Saim")
print("Tuple before deletion: ",tup1)
del(tup1)
# print("Tuple after deletion: ",tup1)  #  ---> error (tup1 does'nt exists)