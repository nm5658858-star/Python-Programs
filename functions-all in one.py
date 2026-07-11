# append count index insert remove reverse pop
a = []
for i in range(3):
    x = input("Enter to loop: ")
    a.append(x)
h = input("Enter to append: ")
g = a.append(h)
print("After appending: ",a)

b = []
for j in range(3):
    y = input("Enter to loop: ")
    b.append(y)
l = input("Enter counting: ")
# print("Original list: ",b)
f = b.count(l)
print(l,"is repeated",f,"times")

c = []
for k in range(3):
    z = input("Enter to loop: ")
    c.append(z)
u = input("Enter to count: ")
f = c.index(u)
print("Index of",u," is: ",f)

d = []
for i in range(3):
    q = input("Enter to loop of index: ")
    d.append(q)
w = int(input("Enter index: "))
ww = input("Enter value: ")
d.insert(w,ww)
print("Inserted:",d)

e = []
for i in range(3):
    r = input("Enter to loop to remove: ")
    e.append(r)
y = input("Enter to remove: ")
t = e.remove(y)
print("Removed",e)

f = []
for i in range(3):
    p = input("Enter to reverse loop: ")
    f.append(p)
print("Original loop is: ",f)
f.reverse()
print("Reversed loop is: ",f)

g = []
for i in range(3):
    u = input("Enter to pop loop: ")
    g.append(u)
print("Before Popping: ",g)
# o = input("Enter to pop: ")
g.pop()
print("After Popping: ",g)

