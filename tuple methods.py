employee = ('Saif',"Malik",101,1.56)
print("1. Len: ",len(employee))

a = (10,20,30,40,50)
print("2. Max: ",max(a))

b = (100,200,300,400,500)
print("3. Min: ",min(b))

c = (10,20,30,45,20,15)
print("4. Index: ",c.index(20))    # always gives first, occuring second 20 ignored

d = (10,20,30,45,20,30)
print("5. Count: ",d.count(30))

# tuple() is used as a constructor which is used to create tuples from
# different types of values

print("1. Creating empty tuple")
tuple()

print("2. Creating tuple from a list")
t = tuple([1,2,3])
print(t)

print("3. Creating tuple from string")
tuple1 = tuple("xyz")
print(tuple1)

print("4. Creating tuple from key of dictionary")
tuple1 = tuple({1:"m",2:"n"})
print(tuple1)

