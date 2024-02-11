# Python-Strings

```python

strings can define
1 ' '
2 " "
3 """ """


>>> chai ="Lemon chai"
>>> print(chai)
Lemon chai
>>> first_chai=chai[0] 
>>> first_chai
'L'

//slicing
>> slice_chai=chai[0:5] 
>>> slice_chai  
'Lemon'

>>> number_list="0123456789"
>>> number_list[:]
'0123456789'
>>> number_list[1:] 
'123456789'
>>> number_list[2:] 
'23456789'
>>> number_list[:2] 
'01'
>>> number_list[2:2] 
''
>>> number_list[0:7:2] 
'0246'
>>> number_list[0:7:3] 
'036'

// lower upper case
>>> print(chai.lower())
lemon chai
>>> print(chai.upper()) 
LEMON 
>>> chai
'Lemon chai'
chai is not change because strings are immutable

// strip
>>> chai ="  Lemon chai  " 
>>> print(chai.strip()) 
Lemon chai


//replace
>>> print(chai.replace("Lemon", "ginger")) 
ginger chai
>>> chai
'Lemon chai'

// split
>>> chai="Lemon, Ginger, Masala, Mint"
>>> chai
'Lemon, Ginger, Masala, Mint'
>>> print(chai.split()) 
['Lemon,', 'Ginger,', 'Masala,', 'Mint']
>>> print(chai.split(", ")) 
['Lemon', 'Ginger', 'Masala', 'Mint']

//find
>>> chai ="Lemon chai"     
>>> print(chai.find("chai"))  
6
>>> print(chai.find("Chai")) 
-1

//count
>>> chai ="Lemon chai chai chai chai" 
>>> print(chai.count("Chai")) 
0
>>> print(chai.count("chai")) 
4

// format
>>> chai_type="Masala"
>>> quantity=2
>>> order ="I order {} cups of {} chai"
>>> order
'I order {} cups of {} chai'
>>> print(order.format(quantity, chai_type))
I order 2 cups of Masala chai

// convert list to string
>>> chai_variety=["lemon", "Masala", "ginger"]
>>> chai_variety
['lemon', 'Masala', 'ginger']
>>> print("".join(chai_variety))  
lemonMasalaginger
>>> print(" ".join(chai_variety)) 
lemon Masala ginger
>>> print("- ".join(chai_variety)) 
lemon- Masala- ginger

//find length
>>> chai="Lemon tea"  
>>> print(len(chai))
9
>>> for letter in chai:
...     print(letter)
...
L
e
m
o
n

t
e
a

//
>>> chai="He said, \"Masala cha is good\" " 
>>> chai
'He said, "Masala cha is good" '

>>> chai="Masala\nchai"
>>> chai
'Masala\nchai'
>>> print(chai)         
Masala
chai
>>> chai =r"Masala\nchai" 
>>> print(chai)
Masala\nchai

>>> chai=r"c:\user\vim" 
>>> print(chai)
c:\user\vim
>>> chai ="Masala\\nchai\\" 
>>> print(chai)
Masala\nchai\

// in
>>> print("Masala" in chai) 
True
>>> print("Masalaa" in chai) 
False
```