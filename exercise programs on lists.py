# print("Program to find sum of elements of List")
# a = []
# b = int(input("Enter how many elements: "))
# for i in range(b):
#     c = int(input("Enter value: "))
#     a.append(c)
# print("List is: ",a)
# sum = 0
# for i in range(b):
#     sum = sum + a[i]
# print("Sum of list elements is: ",sum)


# print("Program to find sum of even & odd elements of List")
# x = []
# y = int(input("Enter number of Elements: "))
# for i in range(y):
#     z = int(input("Enter Number: "))
#     x.append(z)
# print("Original list is: ",x)
# odd = 0
# even = 0
# for i in range(y):
#     if(x[i] % 2 == 0):
#         even = even + 1
#     else:
#         odd = odd + 1
# print("Even is: ",even,", and odd is: ",odd)

print("Program to search an element of List")
l = []
m = int(input("Enter size of list: "))
for i in range(m):
    val = int(input("Enter numbers: "))
    l.append(val)
flag = 0
key = int(input("Enter number to serach: "))
for i in range(m):
    if(l[i] == key):
        flag = 1
        pos = i + 1
        break
if(flag == 1):
    print("Element found at: ",pos," position")
else:
    print("Element not found!")

