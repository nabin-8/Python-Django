# Python internal working

```python

    >>> h1=[1,2,3]
    >>> h2=h1
    >>> h2
    [1, 2, 3]
    >>> h1==h2
    True
    >>> h1 is h2
    True

    next example
    >>> h1=[1,2,3] 
    >>> h2=h1      
    >>> h2
    [1, 2, 3]
    >>> h1        
    [1, 2, 3]
    >>> h1[0]=33
    >>> h1       
    [33, 2, 3]
    >>> h2 
    [33, 2, 3]
    >>> h1 is h2
    True

```
```python

    >>> p1=[0,2,1]
    >>> p2=[0,2,1]
    >>> p1==p2
    True
    >>> p1 is p2
    False

```