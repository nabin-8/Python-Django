# Conditional statement
# temperature =35
# if temperature >30:
#     print("It\'s warm")

# Else if
# age=int(input("Enter your age: "))
# if age>18:
#     print("You are eligible to vote")
# elif age==18:
#     print("You can vote next year")
# else:
#     print("You are not eligible to vote")

# Logical operator
heigh_income=True
good_credit=True
# if heigh_income and good_credit:
#     print("Eligible")
# else:
#     print("You are not eligible")

# another example
# student=False
# if (heigh_income or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not Eligible")

# Age should be between 18 and 65
# age=22
# if age>=18 and age<65: 
#     print("Eligible")

# if 18<=age<65: # Easily implement mathematical expressions
#     print("Eligible")

# Quiz
# if 10=="10":
#     print("a")
# elif "bag">"apple" and "bag">"cat":
#     print("b")
# else:
#     print("c")

# for loop
# for number in range(3):
#     print(number)

# for number in range(1,4):
#     print("Attempt", number, number*".")

# for else
# break => break is used to terminate the loop
# for number in range(1,10):
#     print("Hello")

# Exercise 1
# Print prime number from 1-10
# count=0
# for x in range(1,10):
#     if x%2==0:
#         count+=1
#         print(x)
# print(f"We have {count} even numbers")

# Control-Flow Exercise
""" 
1. Write a program that compares two numbers, a = 10 and b = 20, using different comparison operators (==, !=, <, >, <=, >=). Print the results for each comparison. Explain what comparison operators are and how they are used in control flow.
"""
def comparison():
    while True:
        print("To quit q, Q: ")
        print("To continue y, Y: ")
        program=input(":")
        if(program.lower()=='q'):
            break
        else:
            a=int(input("\nEnter a first argument: "))
            b=int(input("Enter a second argument: "))
            print("\n")
            print("c = compare\ng = greater\nl = less\nn = !")
            comp=input(":")
            if comp.lower()=='c':
                print(f"\n{a == b}\n")
            elif comp.lower()=='g':
                print(f"\n{a > b}\n")
            elif comp.lower()=='l':
                print(f"\n{a < b}\n")
            elif comp.lower()=='n':
                print(f"\n{a != b}\n")
            else:
                print("\nEnter valid string\n")

# comparison()

# qn2
""" 
Write a Python script that assigns a value to a variable result using the ternary operator. If x = 5, set result to "Even" if x is even and "Odd" if x is odd. Discuss how Python's ternary operator (<expression_if_true> if <condition> else <expression_if_false>) works and when it's useful.
"""
# x=int(input("Enter the number: "))
# print("Even number") if x%2==0 else print("Odd number")

