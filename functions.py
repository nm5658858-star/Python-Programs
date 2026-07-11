# # def message():
# #     print("Python Functions!")  
# # message()
# 
# # def add():
# #     a = int(input("Enter first number: "))
# #     b = int(input("Enter second number: "))
# #     c = a + b
# #     print("Sum of given number is: ",a+b)
# # add()
# 
# 
# 
# 
# 
# # def difference(x,y):    # With Arguments
# #     z = x - y
# #    
# 
# 
# def product():          # User defined
#     i = int(input("Enter first number: "))
#     j = int(input("Enter second number: "))
#     pro = i * j
#     print("Product of given numbers is: ",pro)
# product()
# 
# # def table(t):           # With while loop
# #     u = 1
# #     while(u<=10):
# #         print(t,"*",u,"=",t*u)
# #         u = u + 1
# # table(5)
# 
# # def table2():           # With for loop
# #     w = int(input("Enter a number for table: "))
# #     for s in range(1,11):
# #         print(w,"*",s,"=",w*s)
# # table2()
# #-------------------------------------
# #print("1. No Argument With Return")
# def sum():    # sum() = 7
# 
#     i = int(input("Enter first number :"))   #4
#     j = int(input("Enter second number :"))   #3
#     k = i + j    # k =7
#     return k  # 
# add = sum()    # add = 7
# print("Sum is: ",add)
# #--------------------------------------
# print("2. No Argument No Return")
# def even_odd():
#     a = int(input("Enter a number: "))
#     if(a % 2 == 0):
#         print("Number is Even!")
#     else:
#         print("Number is Odd!")
# even_odd()
# # -------------------------------------
# print("3. With Argument With Return")
# def div(a,b):
#     c = a / b
#     return c
# 
# x = int(input("Enter first number: "))   #4
# y = int(input("Enter second number: "))   #3
# division = div(x,y)
# print("Division of ",x,"with",y,"is:",division)
# #---------------------------------------
# print("4. With Argument No Return")
# def condition(i,j,k):  #3,4,5
#     if(i>j and i>k):   
#         print("First number is maximum!")
#     elif(j>i and j>k):
#         print("Second number is maximum!")
#     else:
#         print("Third number is maximum!")
# a = int(input("Enter first number: "))   #3
# b = int(input("Enter second number: "))   #4
# c = int(input("Enter third number: "))   #5
# condition(a,b,c)
# 
# 
# 
# 
# def add(a,b):
#     c = a+b
#     return c
# 
# addition = add(2,3)
# print(addition)
# 
# 

def somefun(a,b,c=3,d):
    e = ((a + b) - (c * d))    # e = 9 - 72
    print(a,"+",b,"-",c,"*",d,"is: ",e)
x = int(input("Enter first number: "))    #6
y = int(input("Enter second number: "))    #7
z = int(input("Enter third number: "))    #8
i = int(input("Enter forth number: "))    #4
# somefun(x,y,z,i)
somefun(4,5,8)
somefun(4,5,2,8)




