# DataTypes in python

# 1.Numeric

    # a. Integer 
num=100
print(type(num))
    # b. Complex Number
    # c. Float
num3=100.55
print(type(num3))

# 2.Dictionary
# 3.Boolean
# 4.Set

# 5.Sequence Type


# a.Strings
# b.List
# c.Tuple
"""
A Python tuple is one of Python’s three built-in sequence data types, the others being lists and range objects. A Python tuple shares a lot of properties with the more commonly known Python list:

    - It can hold multiple values in a single variable
    - It’s ordered: the order of items is preserved
    - A tuple can have duplicate values
    - It’s indexed: you can access items numerically
    - A tuple can have an arbitrary length

    But there are significant differences:
    - A tuple is immutable; it can not be changed once you have defined it.
    - A tuple is defined using optional parentheses () instead of square brackets []
    - Since a tuple is immutable, it can be hashed, and thus it can act as the key in a dictionary
"""
my_numbers = (1, 2, 3)
the_same = 1, 2, 3
my_strings = ('Hello', 'World')
my_mixed_tuple = ('Hello', 123, True)
print(my_numbers, my_strings, my_mixed_tuple)