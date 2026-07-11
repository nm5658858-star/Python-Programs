# 1. len() is used to find length of the Dictionary

# dict1 = {'brand':'Maruti','model':'Dezire','year':2020}
# print(dict1)
# x = len(dict1)
# print("Length of dict1 is: ",x)

# 2. pop() method removes the elements with specified key name

dict2 = {'brand':'Maruti','model':'Dezire','year':2020}
print(dict2)
print("Before popping length is: ",len(dict2))
dict2.pop('model')
print("After popping: ",dict2)
print("After popping length is: ",len(dict2))

# 3. popitem() removes the last element of the dictionary.

# dict3 = {'brand':'Maruti','model':'Dezire','year':2020}
# print(dict3)
# dict3.popitem()
# print("After popitem(): ",dict3)

# 4. del keyword removes the item with specified key name.

dict4 = {'brand':'Maruti','model':'Dezire','year':2020}
print(dict4)
del dict4['brand']
print("After delete keyword: ",dict4)

# 5. del keyword (to delete whole dictionary)

# dict5 = {'brand':'Maruti','model':'Dezire','year':2020}
# print(dict5)
# del dict5
# print("After delete keyword (whole dictionary): ",dict5) --> # raises error (bcz,dict5 is deleted)

# 6. clear keyword (Deletes all the elements of the Dictionary.
# This keyword is also used to delete all the elements of the dictionary.
# Note that it just deletes the content of the dictionary so the dictionary is there but, without any element.

# dict6 = {'brand':'Maruti','model':'Dezire','year':2020}
# print(dict6)
# dict6.clear()
# print("After clear keyword: ",dict6)
# # print(len(dict6)) --> len is 0 but dictionary is still there.

# 7. update() is used to update the dictionary

# dict7 = {'brand':'Maruti','model':'Dezire','year':2020}
# print("Dict7 is: ",dict7)
# dict7.update({'color':'white'})
# print("After update(): ",dict7)

# 8. copy() is used to copy the first dictionary elements into other

# dict8 = {'brand':'Maruti','model':'Dezire','year':2020}
# print("Dict8 is: ",dict8)
# other_dict = dict8.copy()
# print("After copying: ",other_dict)

# 9. fromkeys() methods returns a dictionary within the specified keys,
# and the specified value.

a = ('firstkey','secondkey','thirdkey')
b = 0
dict9 = dict.fromkeys(a,b)
print("After use of fromkeys(): ",dict9)

# 10. setdefault() returns the value of the item with the specified key.
# If the key does'nt exists, it inserts the key, with the specified value.

# dict10 = {'brand':'Suzuki','model':'Dzire','year':2020}
# x = dict10.setdefault("brand","toyota")
# print("Using setdefault() :",x) # Since, "brand" key is already present, so it will return value Suzuki.
# y = dict10.setdefault("city","Faisalabad")
# print("Using setdefault() : ",y) # Since, "city" key was'nt present, so it will insert value Faisalabad.
# print(dict10)
# dict10.update({"city":"Islamabad"})
# print(dict10)

