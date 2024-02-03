# Numbers In Python

1. Integer
1. Float
1. Decimal
1. Fraction
1. complex number
1. sets
1. boolean

```python

>>> x=2
>>> y=3
>>> z=4
>>> x+y
5
>>> x+y*z
14
>>> (x+y)*z
20
>>> 40+2.23  
42.23

type conversion
>>> int(2.23)
2
>>> float(40)
40.0

string concating
>>> "nabin"+"acharya"
'nabinacharya'

>>> x,y,z
(2, 3, 4)
tuple get 

>>> x+1,y*2
(3, 6)
>>> y%2
1

>>> z**2
16

>>> 99999999999999999999999999999999999 +1
100000000000000000000000000000000000

>>> 2**100
1267650600228229401496703205376

>>> 2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
```

numbers are very powerful in python

```python

>>> result=1/3.0
>>> result
0.3333333333333333
```

printing in console in python
```python

>>> repr('nabin')
"'nabin'"
>>> str('nabin')
'nabin'
>>> print('nabin')
nabin
```
boolean in python
```python

>>> 1<2
True
>>> 5.0 == 5.0
True
>>> 4.0 != 5.0
True

>>> x,y,z
(2, 3, 4)
>>> x<y<z
True
>>> x<y and y<z
True
shortcuts
>>> 1 == 2 < 3 
False
>>> 1 == 2 and 2 < 3 
False
```


maths functions in python
```python

>>> import math
>>> math.floor(3.5)
3
>>> math.floor(-3.5) 
-4

>>> math.trunc(3.5)
3
>>> math.trunc(-3.5) 
-3
```
imaginary numbers like in maths
```python

>>> 2+1j
(2+1j)
>>> (2+1j) *3
(6+3j)
```
intresting right python also supports
octal numbers
hexadecimal numbers
binary numbers

```python

note 0o represents octal number in python
>>> 0o20
16
>>> 0o30
24

note 0x represents hexadecimal number in python
>>> 0xFF
255

note 0b represents binary number in python
>>> 0b1000
8
methods to convert
>>> oct(64)
'0o100'
>>> hex(64)
'0x40'
>>> bin(64)
'0b1000000'

using base
>>> int('64', 8)
52
>>> int('64', 16)
100
>>> int('10000', 2) 
16
```
bitwise operations
```python

>>> x=1
>>> x<< 2
4
```

random method in python
```python

>>> import random 
>>> random.random()
0.005003511526601723
>>> random.random()
0.6682387942701605

>>> random.randint(1,100) 
72
>>> random.randint(1,100)
50
>>> random.randint(1,100)
69
>>> random.randint(1,100)
76
>>> random.randint(1,100)
95

>>> l1=['nabin', 'na', 'nb', 'anab', 'nbin']
>>> random.choice(l1)
'nb'
>>> random.choice(l1)
'nabin'
>>> random.choice(l1)
'anab'
>>> random.choice(l1)
'anab'
>>> random.choice(l1)
'na'

>>> random.shuffle(l1)
>>> l1
['na', 'nb', 'anab', 'nabin', 'nbin']
>>> random.shuffle(l1)
>>> l1
['nabin', 'nb', 'nbin', 'na', 'anab']
```

decimal errors or handling decimals in python
```python

problem
>>> 0.1+0.1+0.1
0.30000000000000004
>>> 0.1+0.1+0.1 -0.3
5.551115123125783e-17
>>> (0.1+0.1+0.1) -0.3 
5.551115123125783e-17

solution
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')

decimal context manager to learn more
```

Fraction in Python
```python

>>> from fractions import Fraction 
>>> myFra = Fraction(2, 7)
>>> myFra
Fraction(2, 7)

```

---
Sets in Python
```python

>>> setone={1,2,3,4}
>>> setone & {1,3}
{1, 3}
& refers to intersection

>>> setone | {1,3} 
{1, 2, 3, 4}
| refers to union


>>> setone - {1,2,3,4}
set()
>>> type({})
<class 'dict'>
```

---

Boolean in Python
```python

>>> type(True) 
<class 'bool'>
>>> True == 1
True
>>> True == 0
False
>>> True is 1      
False
>>> True + 4
5
```