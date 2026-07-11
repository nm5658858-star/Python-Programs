# # print("Hello world")
# # Python ke start se start krty hain....
# # comment krny ke liye Alt+3 press krna hai
# # Uncomment ke liye Alt+4
# # commentted line ke liye use hoga => #  
# # print("Hello World") # simple statement to print hello world!
# # # In C++ ==> std::cout<<"Hello World\n";
# # # python mai ; se koi farq nai parta lagao ya na lagao
# # print("Hello Python");
# # C++ mai next line mai jany ke liye "endl" ya "\n" use krna parta hai..
# # Python mai khud hi next line mai chala jata hai...
# # lekin agar hum chahty hain ke next line mai na jaye to usky liye use krna parta hai..ek cheez
# # print("Hello World") # jab yahan tak aye ga to python khud hi usko next line mai bhej de ga
# # next line mai na jaye to usky liye....
# # print("Hello World",end = "") # end = "" use hoga
# # print("Hello Saba")
# 
# 
# # C++ mai jab hum koi value likhna chahty thy to pehle data type likhna hoti thi
# # Jese ke...
# # int a = 5
# # float b = 55.5
# # string c = "Hello"
# # char d = 'a'
# # But in Python, compiler khud hi decide krleta hai ke kis type ka data hai
# # for example:
# 
# # a = 5
# # print(a) # ==> 5 aik integer hai to wo khud hi decide krly ga...Python compiler(PC)
# 
# # C++ syntax :
# #     int a = 5;
# #     std::cout<<a<<endl; # ==> 5
# # ya aisy bhi likhty thy...
# # int x = 10;
# # std::cout<<"Value of x is: "<<x<<endl;
#  
#  
# 
# # x = 10
# # print("Value of x is: ",x)
# # y = 55
# # print("Value of x is: ",x,"and value of y is: ",y)
# # y = 66
# # print("Value of x is: ",x,"and value of y after changing is: ",y)
# # 
# # i = input("Enter something: ") # for any type of user input
# # # but for input jo sirf integer type ki honi chahiye to usky liye humy..
# # j = int(input("Enter an integer: ")) # ==> int mai convert krna hoga
# 
# # because Python humy facilitate krta hai following:
# # 1. add int into int
# # 2. add string into string
# 
# # i = "My name is Saba" # is a string
# # j = "I study in GCUF" # is also a string
# # k = ("String + string is: ",i+j) 
# 
# # i = input("Enter name: ")
# # j = input("Enter city: ")
# # print("String + string is: ",i+j) # adds string into string
# 
# # x = int(input("Enter first int: "))
# # y = int(input("Enter second int: "))
# # z = x + y
# # print("Sum of integers is: ",z) # adds two integer
# # 
# # to hum jab aik string ko int ke sath add krny ki koshish kren ga to aik error aye ga...
# # thus hum ko int mai convert krny ke liye ye statement likhna hogi
# # y = int(input("Enter second int: "))   # got it?....Hmmm?
# # ya to dono string honi chahiye ya dono int
# # 
# # jab hum aisy likhen ga ...
# # j = input("Enter city: ")
# # to is mai kisi bhi type ka data aa sakta hai...
# # lekin jab hum chahty hain ke sirf integer type ka data store krna hai...
# # y = int(input("Enter second int: "))
# # to ye likhen ga.....
# 
# 
# 
#     
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# # agla dekho
# # jab user se input lete thy to c++ mai kehty thy:
# #
# # c++ mai syntax user se input lene ka..:
# # int i;
# # cout<<"Enter a number: ";
# # cin>>i;
# # cout<<"Value of I is: "<<i<<endl;
# 
# # python case mai, user se value input krny ke liye...
# 
# # i = input("Enter a number :")
# # print(i)
# # # is mai hum kisi bhi cheez ka input le sakty hain yaani string integer ya float
# # j = input("Enter your name: ")
# # print("Your name is: ",j)
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# print("Starting with for loops")
# 
# 
# # IN C++, syntax of for loop:
# # 
# # for(int i = 1;i<10;i++){
# #     cout<<i<<endl;
# #     }
# 
# 
# # Python mai for loop aik given range tak jaati hai..
# # Range  hum dete hain
# for i in range(10):    # i variable hai in range yaani iski range tak  .... jo range hai us se aik kam tak print hoga iss case mai 0 to 9
#     print(i)
# 
# 
# 
# 
# 
# 
# 
# 
# In Python, syntax is as:
# for i in range(10):    # jo range di hai wahan tak print karo i.e. 10
#     print(i)    # indentation is necessary
#     print(i+1)     # will print till 10, starting from 1
# # lekin python aik subtract krky print krta hai... yaani jo number dia hai us se aik kam tak i.e. 9 , starting from 0

# for i in range(10):
#     print(i)             #here by default, start is 0, end is given that is 10 and by default increases by 1
# for j in range(0,10,1):      #(starting value, ending value, step value) ==> start from 0, end at 10, increase by 1
#     print(j)

# print("Print even numbers only: ")
# for n in range(0,20,2):     # step value is 2 so it increases 2,   yaani aik number chorr kar agla
#     print(n)

x = int(input("Enter a number: "))
for y in range(x):     # x jo number enter kiya hai wahan tak loop chalao
    print(y)

