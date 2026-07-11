# a = int(input("Enter a number: "));
# if(a%2 == 0):
#     print("Even number! ");
# else:
#     print("Odd number! ");
    

# b = int(input("Enter your age: "));
# if(b>=18):
#     print("You are eligible for voting!");
# else:
#     print("You are'nt eligible for voting!");


#             program for a max number
# i = int(input("Enter first number: "));
# j = int(input("Enter second number: "));
# k = int(input("Enter third number: "));
# if((i>j) and (i>k)): 
#     print("First number entered is greater!");
# elif((j>i) and (j>k)):       # colon(:) after condition is necessary
#     print("Second number is greater!")     # semicolon(;) after statement(s) is'nt necessary
# elif((k>i) and (k>j)):
#     print("Third number is greater!")
# else:
#     print("Numbers are equal!")   
    
    
# x = int(input("Enter a number: "));
# if(x>0):
#     print("Number entered is positive!");
# elif(x<0):
#     print("Number entered is negative!");
# else:
#     print("Number entered is zero!");


# a = int(input("Enter first number: "));    # lets say first number is = 5
# b = int(input("Enter second number: "));   # lets say first number is = 900
# c = int(input("Enter third number: "));    # lets say first number is = 122
# if((a>b and a<c) or (a<b and a>c)):        #check whether -> (5>900 and 5<122) or (5<900 and 5>122)
#     print("A is middle",a);
# elif((b>a and b<c) or (b<a and b>c)):      #(900>5 and 900<122) or (900<5 and 900>122)
#     print("B is middle",b);
# else:
#     print("C is middle",c);                #122 is middle


    
sub1 = int(input("Enter subject1 marks: "));
sub2 = int(input("Enter subject2 marks: "));
sub3 = int(input("Enter subject3 marks: "));
sub4 = int(input("Enter subject4 marks: "));
sub5 = int(input("Enter subject5 marks: "));
fullmarks = 500;
totalmarks = (sub1 + sub2 + sub3 + sub4 + sub5);
print("Total obtained marks are: ",totalmarks);
percentage = (totalmarks/fullmarks)*100;
print("Percentage of obtained marks is:",percentage);
if(percentage>=80):
    print("You have got grade A!");
elif(percentage>=60):
    print("You have got grade B!");
elif(percentage>=40):
    print("You have got grade C!");
else:
    print("You have got grade D!");
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    