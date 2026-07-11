print("Change values")
dict1 = {"brand":"Suzuki","model":"Dzire","year":2020}
print("Before changing:",dict1)
dict1["year"] = 2022
print("After changing:",dict1)

print("Checking whether a key exists in the Dictionary")
dict2 = {'brand':'Nike','model':'Dezire','year':2020}
print(dict2)
if 'model' in dict2:
    print("Yes, 'model' is one of the keys in the dictionary")
else:
    print("No, 'model' is not one of the keys in the dictionary")

print("Adding new elements in the Dictionary")
print(dict1)
dict1['color'] = 'white'
print("After adding: ",dict1)

