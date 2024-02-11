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

tea_varities.remove("Green")
>>> tea_varities
['Black', 'Oolong', 'White']

>>> tea_varities.insert(1,"Green")
>>> tea_varities
['Black', 'Green', 'Oolong', 'White']


//copy
>>> tea_varities_copy=tea_varities.copy()
>>> tea_varities_copy
['Black', 'Green', 'Oolong', 'White']

//append
>>> tea_varities_copy.append("Lemon")
>>> tea_varities_copy
['Black', 'Green', 'Oolong', 'White', 'Lemon']
>>> tea_varities
['Black', 'Green', 'Oolong', 'White']

//range
>>> squard_nums = [x**2 for x in range(10)] 
>>> range(10)
range(0, 10)
>>> y= range(10)
>>> y
range(0, 10)

>>> squard_nums                            
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> cube_number=[y**3 for y in range(5)] 
>>> cube_number 
[0, 1, 8, 27, 64]
```