# Python

#### 01 - Introduction to Python
#### 02 - Python Installation and Setup
#### 03 - Python Datatypes
#### 04 - Operators and Expression
#### 05 - Conditional Statements
#### 06 - Loops - Control Flow
#### 07 - String and its Methods
#### 08 - Formatted Printing
#### 09 - Regular Expression
#### 10 - List
#### 11 - Tuple
#### 12 - Sets
#### 13 - Dictionary
#### 14 - Functions
#### 15 - More About Functions
#### 16 - Exception Handling
#### 17 - File Handling
#### 18 - Object Oriented Programming
#### 19 - MultiThreading
#### 20 - Date and Time
#### 21 - DataBase Connectivity
#### 22 - Data Structure Modules
#### 23 - Math Modules
#### 24 - OS Module
#### 25 - Tkinter
#### 26 - NumPy Arrays
### Python Core

1. Introduction to Python 30m 47s
1. Installation and Setup 16m
1. Python Virtual Machine (PVM) 22m 59s
1. Create and Run Python Program 28m
1. Comments in Python 9m 19s
1. Data 14m 1s
1. Variables and Data Types 3Im 14s
1. Memory Management 24m 43s
1. print method 31m 58s
1. Keywords and Import 25m 25s
1. Type Conversion and Number System 55m 48s
1. Taking Input From User 15m 47s
1. Operators Part-1 36m 595
1. Operators Part-2 24m 35s
1. Operators Part-3 22m 38
1. Decision Control 40m 48s
1. match statement 17m 1s
1. while loop 37m 8s
1. Transfer Control: break, continue and pass 30m 45s
1. for Loop 19m 43s
1. Range 46m 14s
1. List Part-1 23m 33s
1. List Part-2 30m 21s
1. List Part-3 28m 10s
1. str Part-1 22m 17s
1. str Part-2 27m 29s
1. tuple 26m 2s
1. set 43m 5s
1. dict 26m 455
1. Functions 28m dls
1. Default Arguments 10m 33s
1. Keyword Arguments 13m 18s
1. Variable Length Arguments 6m1s
1. Recursion 27m 48s
1. lambda Expression 17m 28s
1. Variable length keyword arguments 16m 44s
1. map, reduce and filter 15m 48s
1. Decorators 17m 44s
1. Introduction to OOP 36m 57s
1. Classes and Objects 13m 30s
1. init method 23m 43s
1. Types of Methods 32m 39s
1. Types of Variables 28m 28s
1. Inheritance 48m 28s
1. Name conflict Issues 36m 555
1. Polymorphism 6m 37s
1. Name Mangling 9m 65
1. Operator Overloading 14m 38s
1. Local and Global Variables 18m 37s
1. Exception Handling 49m 255
1. User defined exception 29m 10s
1. Iterators and Generators 28m 39s
1. File Handling 41m 23s

##
#### Introduction to Python
##### History of Python
- Python was conceived in the late 1980s by Guido van Rossum at centrum wiskunde and Informatica in the Netherlands as a successor at the ABC language.
- He has been invariably worked as the lead developer, until 12 July 2018.
- In Jan 2019, active Python core developers elected a five member council to lead the project.

- Name- Python
- Python developers aim for it to be fun to use. The name Python is a tribute to be the British comedy groupe *Monty Python*.

##### Version History of Python
<pre>
Python 1.0 1994
Python 2.0 2000
Python 3.0 2008
Latest Version
Python 3.10.6 2 Aug 2022
</pre>
##### Why you should learn Python?
- Huge Community Support.
- Future is with AI.
- Easy to learn and implemented.
- General Purpose Programming Language.
- Any type of GUI and CLI applications easily made.
- Many Library and Frameworks avilable.

##### Features of Python
- Highly Extensible
- Simple and straight forward syntax
- multi-paradigm programming language
- Emphasis on code readability
- Dynamic Typing
- Automatic memory management.
- Dynamic Building
- Precise Coding
- For time critical operations, python can use methods written in c language.
- Indentation base block of code.
- Large Library
- Platform independent.
##### Amazing Facts
- Ranked #1 (TIOBE)
- Highest rise in rating 2007, 2010, 2018, 2020
- It reduces app development time by 1/6
- Large organizations that was Python are Google, Netflix, Dropbox, Youtube, Instagram, CERN, Microsoft, NASA, Amazon, Facbook, etc
##### Where Python can be used?
1. Developing Websites
1. Task automation
1. Data Analysis
1. Data Visulization
1. AI, ML, IOT
1. Developing Desktop applications
- Python can also be used in developing mobile applications, clint side of AJAX based applications.
##### Learning Path
- Core Python
- OOP
- Frameworks

##
#### Installation and Setup
1. Visit python website
1. Select your Operating System or direct click on download python button
##### Download Python
##### Install Python
##### Verify Installation
##### Download VS Code
##### Install VS Code
##### Setup Python on vs code
1. Code Runner
1. Python Pack

##
#### Python Virtual Machine (PVM)
##### How to develop applications using C/C++?
- Computer can only understand machine language.
- Machine code are OS dependent
- OS
Python.org
Welcome to Python.org

The official home of the Python Programming Language

oun

- Doctor ---> Common noun class
- Dr.Suraj --> Proper noun object

##### Name in namespace
- Name in namespace is a variable which is used to contain id(reference) of
1. Instance object
1. Function object
1. class object
- In Python everything is an object

##
#### print method
##### Agenda
1. print()
1. sep
1. end
1. Special Characters
1. Format Specefiers

##### print()
- print simple text print("Welcome")
- print variable value print(x)
- print expression print(x+5*3)
- print multiple value print(x,y)

##### sep
- By default seperator is space
Python

print(a,b,c)
5 6 7
- if we have to change seperator?
- we use the sep
Python

print(a,b,c,sep=',')
5 6 7
print(a,b,c,sep='-',end='!')
##### Special Characters
Python

'\n' new line
'\t' tab
'\b' backspace
'\r' Carriage Return
'\\' print \
'\"' print "
"\'" print '
print("Hello\nWorld")
print("Hello\b\bWorld")

##### Format Specefiers
Python

print("Value of x is",x)
value of x is 5
print("value of x is %d"%(x))
print("value of x is %d and value of y is %d"%(x,y))
##
#### Keywords and Import
##### Agenda
1. What is Module in Python?
1. import
1. Keywords
1. help() on python shell

##### Module, Package and Library
1. module: It is a python file. It can contain instance objects, function objects and class objects.
    - It simple words. it contains variables functions and classes
1. package: package is a collection modules and seb packages.
1. Library: Library is a collection of packages.

##### import
<pre>
import A2
moduleName.moduleElement
moduleElement can be
- variable(Instance object)
- function
- class
</pre>
Python

# import A2
# from A2 import x
from A2 import x as y
x=2
print("x variable from A1: ",x)
print("x variable from A2: ",y)
##### Keywords
- Predefined words
- Reserved words
Python

False   class       from        or
None    continue    global      pass
True    def         if          raise
and     del         import      return
as      elif        in          try
assert  else        is          while
async   except      lambda      with
await   finally     non local   yield
break   for         not
- Keyword.py kwlist

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
- help()
- keywords
F
Python

alse               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not       
```