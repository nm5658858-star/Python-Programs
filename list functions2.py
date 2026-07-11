#append() is used to append (add) a passed object at the end of the list.
# Note that the object is added to last of the list.
# a = ["Saif", "Hamza", "Asfand", "Kela"]
# print(a)
# a.append("Anyone")
# print("After Append() is: ",a)


# print("Program to implement append() method")
# a = []
# for i in range(5):
#     x = input("Enter item to add to list: ")
#     a.append(x)
# print(a)


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
# for i in range(2):
#     print(a[i])
# for i in a:
#     print(i)
#-----------------------------
# count() is used to count the frequency of a given object.
# Frequency refers to kitni baar aya aik specific object!

# a = ["Saif", "Malik", "Saif", "Hamza","Rana"]
# x = a.count("Saif")
 
# print("Frequency =",x,". It means, Saif is repeated ",x," times")
# x = a.count("Hamza")
# print("Frequency of Hamza = ",x)
# r = a.count("Rana")
# print("Frequency of Rana = ",r)

# print("Program to implement count() method")
# a = []
# for i in range(5):
#     x = input("Enter item to add to list: ")
#     a.append(x)
# y = input("Enter value whose frequency you want: ")
# f = a.count(y)
# print(a)
# print(y, "is repeated ",f, " times")
#--------------------------------

# index() is used to find the index of the object/element.
# This function returns the first index of the object/index
#  If it is found, otherwise it returns an exceptions showing that the element is not found.

# a = ["Saif", "Malik", "Saif", "Hamza"]
# x = a.index("Hamza")
# print("Index of Hamza =",x)    #0=Saif,1=Malik,2=Saif,3=Hamza

# print("Program to implement index() method")
# a = []
# for i in range(5):
#     x = input("Enter item to add to list: ")
#     a.append(x)
# y = input("Enter value to find index: ")
# z = a.index(y)
# print(a)
# print(f"{y} is on {z} index")
#--------------------------------


# insert(index, objext) is used to insert an object/value at the given index
# a = [5,"Saif",10]
# a.insert(2,"Malik")    # second index pr Malik insert kro

# print("Program to implement index() method")
# a = []
# for i in range(5):
#     x = input("Enter item to add to list: ")
#     a.append(x)
# print("Original list is: ",a)
# index = int(input("Enter index where you want to insert: "))
# value = input("Enter value to insert: ")
# a.insert(index,value)
# print("List after insertion",a)
#--------------------------------

#remove(object) is used to delete an object value from the given list.
#Note that it removes the first occurence of list.
# a = [5,"Saif",10,"Malik",10]
# a.remove(10)
# print(a)
# 
a = []
for i in range(5):
    x = input("Enter item to add to list: ")
    a.append(x)
print("Original list is: ",a)
value = input("Enter value to remove: ")
a.remove(value)
print("List after deletion",a)
#--------------------------------

# reverse() is used to reverse the elements  present in the lis in place.
# Here the wrod "in place", means that the list gets reversed itself.
# a = ["Saif",5,"Malik",10,99.99]
# a.reverse()
# print(a)
# 
# a = []
# for i in range(5):
#     x = input("Enter item to add to list: ")
#     a.append(x)
# print("Original list is: ",a)
# a.reverse()
# print("Reversed list is",a)
#---------------------------------

# pop() is used to delete the last element from the list.
# Note that this function deletes the last element from the list one-by-one.
# a = [1,2,3,4,5]
# a.pop()
# print(a)
# a.pop()
# print(a)

# a = []
# for i in range(5):
#     x = input("Enter item to add to list: ")
#     a.append(x)
# print("Original list is: ",a)
# a.pop()
# print("After popping is: ",a)

