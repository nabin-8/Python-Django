# primitive data_types
students_count=1000
rating=4.99
is_published = True
course_name = 'Python Programming'

print(students_count, type(students_count))
print(rating, type(rating))
print(is_published, type(is_published))
print(course_name, type(course_name))

students_count="hrkko"
age:int=10
name:str="Nabin"
print(f"My Name is {name} and age is {age}")

age=name
print(age)
# print(name[0]='j') # cannot assigned


# string method to find and replace
def find_replace(sentence,word_to_find, word_to_replace):
    return sentence.replace(word_to_find,word_to_replace)

# print("I love you Python")
# word_to_find=input("Enter Word to find: ")
# word_to_replace=input("Enter Word to replace: ")
# print(find_replace("I love you Python", word_to_find, word_to_replace))

def formatted_details(name, age, profession):
    return f"My name is {name}, I am {age} years old, and I work as an {profession}"

name=input("Enter your name:")
age=input("Enter your age:")
profession=input("Enter your profession:")
print(formatted_details(name, age, profession))