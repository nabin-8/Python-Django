
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
def fizz_buzz(input):
    if (input%3==0) and (input%5==0):
        return "Fizz Buzz"
    elif input%5==0:
        return "Buzz"
    elif input%3==0:
        return "Fizz"
    else:
        return input


input_num=int(input("Enter the Number: "))
print(fizz_buzz(input_num))
# def get_greeting(name):
#     return f"Hi {name}"


# message=get_greeting("Nabin")
# file=open("content.txt", "w")
# file.write(message)