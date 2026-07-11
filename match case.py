x = int(input("Enter first operand: "))
y = int(input("Enter first operand: "))
ch = input("Enter an operator (=,-,*,/): ")
match (ch):
    case '+':
        print(x,"+",y,"=",x+y)
    case '-':
        print(x,"-",y,"=",x-y)
    case '*':
        print(x,"*",y,"=",x*y)
    case '/':
        print(x,"/",y,"=",x/y)
    case _:
        print("OOPS! Invalid operator!")
