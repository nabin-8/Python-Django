# List In python

```python

in different languages list called as array
python call it as a list
>>> tea_varities=["Black","Green","Oolong","White"]
>>> tea_varities
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varities[-1]) 
White
>>> print(tea_varities[1])  
Green
>>> print(tea_varities[2]) 
Oolong

>>> print(tea_varities[1:3]) 
['Green', 'Oolong']
>>> print(tea_varities[:2])  
['Black', 'Green']

>>> tea_varities[3]="Herbal" 
>>> print(tea_varities)      
['Black', 'Green', 'Oolong', 'Herbal']


>>> tea_varities[1:2]="Lemon" 
>>> tea_varities              
['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
>>> tea_varities=["Black","Green","Oolong","White"]
>>> tea_varities               
['Black', 'Green', 'Oolong', 'White']
>>> tea_varities[1:2]=["Lemon"] 
>>> tea_varities
['Black', 'Lemon', 'Oolong', 'White']

>>> tea_varities[1:3]        
['Lemon', 'Oolong']
>>> tea_varities[1:3]=["green", "Masala"]
>>> tea_varities      
['Black', 'green', 'Masala', 'White']

>>> tea_varities=["Black","Green","Oolong","White"]
>>> tea_varities[1:1]        
[]

>>> tea_varities[1:1]=["test", "test"]
>>> tea_varities     
['Black', 'test', 'test', 'Green', 'Oolong', 'White']

>>> tea_varities[1:3]=[]
>>> tea_varities        
['Black', 'Green', 'Oolong', 'White']
>>> for tea in tea_varities:
...     print(tea)
...
Black
Green
Oolong
White
>>>

>>> for tea in tea_varities:
...     print(tea, end="*")  
...
Black*Green*Oolong*White*


>>> if "Oolong" in tea_varities:
...     print("I have Oolong tea")
...
I have Oolong tea

>>> tea_varities.append("Lemon")   
>>> tea_varities                   
['Black', 'Green', 'Oolong', 'White', 'Lemon']
>>> tea_varities.pop()             
'Lemon'
>>> tea_varities       
['Black', 'Green', 'Oolong', 'White']
```