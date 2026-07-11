 
# x = "I AM GOING TO MARKET TO BUY SOMETHING"    # len = 20   0 -19
# y = "TO"
# print("length is: ",len(x))    #20 - 1 = 19 0-19
# print(x.find(y,12,len(x) -1))     # print(x.find(TO,0,18)


 
# # Find the index of "world"
# index1 = my_string.find("world")
# print(f"Index of 'world': {index1}")    
# print("Index of 'world' : ",index1)
# string = "Hello, world! Welcome to Python."
# # Find the index of "Python" within a specific range
# index2 = string.find("Python", 20, 31)    #25
#     
# print("Index of Python is: ",index2)    #25
# # Attempt to find a substring that doesn't exist
# index3 = string.find("Java")
# print(f"Index of 'Java': {index3}")   #-1

#----------------------------------------
# a = "Saif Malik"
# print("Length of string is: ",len(a))
# b = input("Enter your name: ")
# print("Length of ",b," is: ",len(b))
# c = input("Enter your name: ")
# for i in range(0,len(c)):
# #     print(c)
#     print(c[i], end = '')
#-----------------------------------
# 
# print("Step 1 for reverse string: ")           # | -3| -2| -1
# a = input("Enter string: ")                       # | R | a | m
#                                                                 # | 0 | 1 | 2
# print(a[0:])    # 0 se end
# print("String is: ",a)
# print(a[-1::-1])      # start value = -1, end value = start tak, step value -1 m...-2 -3

## -1 start value hai 
## End value nai di hui is liye wo jaye ga wahan tak, jahan tak string end nai hoti ( from "m" to "R")
## -1 step value hai yaani -1 se increase kro, to -1-1 = -2 (-2 = a) ab "a" print hoga, and so on....
#-----------------------------------------------------

# print("Step 2 for reverse string: ")
# b = input("Enter string: ")
# print(len(b)) #  5                        Saba
# for i in range((len(b) -1) ,-1, -1):      # 
#     print(b[i], end = '')

#-----------------------------------------
# print("Check number of consonants & vowels in a string")
# cv = input("Enter string: ")
# vowel = 0
# consonant = 0
# print(cv,"'s no. of len = ",len(cv))
# for i in range(0,len(cv)):
#     if(cv[i] != " "):
#         if(cv[i] == "a" or cv[i] =="e" or cv[i] == "i" or cv[i] == "o" or cv[i] == "u"
#            or cv[i] == "A" or cv[i] == "I"
#            or cv[i] == "O" or cv[i] == "U" or cv[i] == "E"):
#              vowel = vowel + 1
#         else:
#             consonant = consonant + 1
# print("Total number of vowels are: ",vowel)
# print("Total number of consonant are: ",consonant)
#--------------------------------------------------------------
# If reverse of a string is same as actual string, then it is called a Palindrome string!
# print("Check if a string is palindrome or not")
# p = input("Enter string: ")
# q = p[-1::-1]
# if(p == q):
#     print(q," is Palindrome!")
# else:
#     print(q, "is Not Palindrome!")
