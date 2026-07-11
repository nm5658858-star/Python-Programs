# 1. Using tuple display constructs
# tuple1 = () # empty tuple
# tuple2 = (val1, val2,...)

# 2. Creating empty tuple
# tuple1 = tuple()

# 3. Creating single elements tuple
# tuple1 = (2) => this will not be a tuple but an integer class
# tuple2(2,)   => this will be a tuple class
# Here after the element you need to give a comma(,)

# print("Demo")
# t1 = (1)
# print(type(t1))
# t2 = (1,)
# print(type(t2))

# 4. Creating Tuple from Existing Sequences
# We can also use a built-in tuple type object(tuple()) to create tuples from sequences as per the syntax:
# tuple1 = tuple(<sequence>)

# Sequences can be of any types like strings, lists and tples.
# -----> Creating tuple from strings.
str = "World"
t1 = tuple(str)
print("String converted into tuple: ",t1)
# OUTPUT: ('W','o','r','l','d')

# -----> Creating tuple from list
list1 = [1,2,3,4,5]
tuple1 = tuple(list1)
print("List converted into tuple: ",tuple1)
# OUTPUT: (1,2,3,4,5)

# Different types of tuples
# ---------------------------------------------------------------------
#| Ways to create tuple             |     The type of tuple            |
# ---------------------------------------------------------------------
#| ()                                            |     This is an empty tuple   |
#| (7,)                                         |     Tuple with one element |
#| (1,2,3)                                     |     Tuple of integers            |
#| (1,2,3.4,5)                               |    Tuple of numbers            |
#| ('a','n','d')                               |     Tuple of characters         |
#| ('a',1,2,3.5,'you')                     |     Tuple of mixed data type|
#| ('Saba','Saif','Ali')                   |     Tuple of string                |
# ---------------------------------------------------------------------
