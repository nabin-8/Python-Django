# 1.defining function
# def greeting():
#     print("Hello, World!")


# # Calling the function
# greeting()

# 2. Argument
# parameter
# def greet(user_name):
#     print("Hi There"+user_name)


# greet("Nabin")
# # argument

# 3. Types of Functions
# 1. Perform a task
# 2. Return a value

def greet(name):
    print(f"Hi {name}")
    
# greet and print are type1
# round(1.9) is the example of return type

def greeting(name):
    return f"Hi {name}"


# 4. keyword argument
def increment(number, by):
    print(number+by)


# print(increment(10,2)) # 12 and none
# 5. Default Argument
def decrement(number,by=1):
    return number-by


# print(decrement(10))
# xargs
def multiply(*numbers):
    print(numbers)
    total=1
    for number in numbers:
        total*=number
    print(total)


# multiply(5,5)
# 7. xxargs
def save_user(**user):
    print(user)


# save_user(id=1,name="John", age=22)
# Global Variable
# name="Nabin"

# Debugging
# def multiply(*numbers):
#     total=1
#     for number in numbers:
#         total*=number
#     return total


# print("Start")
# print(multiply(1,2,3))


# Exercise: Buzz-Fizz
# def fizz_buzz(input):
#     if (input%3==0) and (input%5==0):
#         return "Fizz Buzz"
#     elif input%5==0:
#         return "Buzz"
#     elif input%3==0:
#         return "Fizz"
#     else:
#         return input


# input_num=int(input("Enter the Number: "))
# print(fizz_buzz(input_num))
# def get_greeting(name):
#     return f"Hi {name}"


# message=get_greeting("Nabin")
# file=open("content.txt", "w")
# file.write(message)

# Function Exercise
# 1. Shopping Cart with args:
""" 
Write a function shopping_cart(*items) that accepts a list of items as arguments and prints each item. Demonstrate how to call this function with multiple items.
"""

def shooping_cart(**items):
    for item in items:
        print(item)


shooping_cart(mouse=500, watch=6000, laptop=898458)