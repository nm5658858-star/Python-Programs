print("Dictionaries in Python!")
# Dictionary is a collection which is unordered, changeable, and indexed.
# In Python, dictionaries are written within curly brackets, and they have keys
# and values.
# Means the dictionary contains two things:
# First is the key
# Second is the value
# 
# d = {1:"Saba",2:"Saif"}
# print(d)
# print(type(d))
# 
# 
# dict = {"brand":"Suzuki","model":"Dzire","year":2020}
# print("Print dictionary",dict)



# You can access the items of a dictionary by refering to its key name inside[]

# dict1 = {"brand":"Suzuki","model":"Dzire","year":2020}
# print(dict1)
# x = dict1["brand"]
# print("Accessing item:",x)


# There is also called a method called get() for the same task
# dict2 = {"brand":"Suzuki","model":"Dzire","year":2020}
# print(dict2)
# x = dict2["model"]
# print("By first method:",x)
# y = dict2.get("model")
# print("By get() method:",y)


# print("Loop through a dictionary")
# dictionary = {"brand":"Suzuki","model":"Dzire","year":2020}
# for x in dictionary:
#     print(x)                      # Will print index values
#     print(dictionary[x])    # Will print the values
# 
# print("Use the values() function")
# for x in dictionary.values():
#     print(x)                # Will also print the values

print("Use of items() function")
dict3 = {"brand":"Suzuki","model":"Dzire","year":2020}
for x,y in dict3.items():
    print(x,":",y)

