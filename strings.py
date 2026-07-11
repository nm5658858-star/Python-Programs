# # name = "Saif"
# # print(name)    #Saif
# # 
# # name2 = "Malik"
# # print(name2)     #Malik
# # print(name2[0])  # name2[0] ==> M
# # for i in name2:
# #     print(i)     
# #     print(i,end = '')
# 
# # for i in range(5):
# #     print(name2[i],end='')
# 
# #-----------------------------------
# print("Concatenation Operator: +")
# x = "Every" + "day"
# print(x)
# 
# print("Replication Operator: *")
# y = 3*"Hello"
# print(y)
# 
# print("Membership Operator: in/not in")
# z = "a" in "Hamza"
# print(z)
# z = "y" in "Saif"
# print(z)

#-----------------------------------

# a = "Hello World"
# print(a[4:-2])    # o Wor

# b = "Hello World"
# print(b[6:],b[:6])

# print("String Slicing") #| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
# str = "Hello World"     #| H | e | l | l | o |   | W | o | r | l | d  |
# print(str[6:10])             #|                             | W   o   r   l
# print(str[6:1])               #|                         
# print(str[4:])                #|                    | o |   | W   o   r   l   d  |
# print(str[3:-2])             #|                    | l | o |   | W   o   r |
# print(str[:-5])               #| H | e | l | l | o |   |
# print(str[:5])                 #| H | e | l | l | o | --------->[0:5-1] = [0:4]

#-----------------------------------------------------------------------

str = "Hello World" # ye aik string hai
# agar hum ne iske kuch words ko ya  letters ko print krwana hai to us ke different ways hain..
print(str[6:10])         #| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
                                #| H | e | l | l | o |   | W | o | r | l | d  |
print(str[4:])
# yahan hum keh rahy hain ke 4th index se start karo or last tak jao
print(str[3:-2])

pehle negative slicing bhi dekh lo...positive to wo hai jo uper hai...
negative slicing start hogi right side se lekin -1 se
yaani d pr index hai -1
l slicing pe hai
# yahan hum keh rahy hain ke 3rd index se start karo or




# print(str[6:10]) # 6:10 ka matlab hai ke 6th index se start karo or 10th index tak jao
# yaani, W se start karo or d tak jao yaani World print karwao
# ab yahan d print q nai hua?
# jesa ke hum ne dekha tha ke for loop aik peeche tak print krwata tha..
# for i in range(10) mai wo 0 se 9 tak jata tha issi tarah idr bhi hai



# ye dekho ye indexes ke niche unki jagah hai..yaani 0 indes pe H hai or 1 pr e and so on..
# ab hum ne print krwana hai koi khaas index se le kar aik specific index tak instead of whole string
# to hum kya kren ga.. jese for loop mai dekha tha naa... for i in range(0,10,1)
# 0 start value thi , 10 end value or 1 step value ...ussi tarah ye bhi hai







