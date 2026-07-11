# def factorial(n):
#     '''It is a factorial program'''
#     if (n == 1 or n == 0):
#         return 1
#     else:
#         return (n * factorial(n-1))
# fact = int(input("Enter a number to calculate factorial: "))
# print(factorial(fact))
# print(factorial.__doc__)    # doc strings (ye yaad hai?)
# print()

def print_numbers(n):
    if n == 0:   
        return
    print_numbers(n-1)   
    print(n)             


num = int(input("Enter a number: "))
print_numbers(num)







# i = int(input("Enter a number: "))    # 5
# j = i
# n = 0
# f = 1
# while(n<i):
#     f = f *i
#     i = i - 1
# print(f"Factorial of {j} is: {f}")