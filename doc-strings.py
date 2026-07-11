'''Hello, World!'''

def square(n):
    ''' It takes a number and gives the square of it'''
    print(n*n)
n = int(input("Enter a number: "))
square(n)
print(square.__doc__)