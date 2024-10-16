from abc import ABC, abstractmethod
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
        
        
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")
        
        
# point=Point(1,2)
# point.draw()


# class vs instance attributes
# class Point:
#     default_color="red"
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
        
        
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")
        

# Point.default_color="yellow"
# point=Point(1,2)
# print(point.default_color)
# print(Point.default_color)
# point.draw()

# another=Point(3,4)
# another.default_color="red"
# print(another.default_color)
# another.draw()


# Creating custom data structure / container
class TagCloud:
    def __init__(self):
        self.__tags={}
    
    def add(self, tag):
        self.__tags[tag.lower()]=self.__tags.get(tag.lower(),0)+1
    
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(),0)
    
    def __setitems__(self, tag, count):
        self.__tags[tag.lower()]=count
        
    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
        return iter(self.__tags)

cloud=TagCloud()
# cloud.add("Python")
# cloud.add("python")
# # cloud["python"]=10
# cloud.add("python")
# cloud.add("nabin")
# cloud.add("Nabin")
# cloud.add("python")
# cloud.add("python")
# print(cloud.__tags)
# print(len(cloud))

# print(cloud.__dict__)
# print(cloud._TagCloud__tags)


class Product:
    def __init__(self, price):
        self.price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value<0:
            raise ValueError("Price cannot br negative.")
        self.__price=value


# product=Product(-10)
# print(product.price)



class Animal:
    def __init__(self):
        self.age=1
    
    def eat(self):
        print("eat")

# Animal: Parent, Base class
# Mammal: Child, Sub class

class Mammal(Animal):
    def walk(self):
        print("walk")

        
class Fish(Animal):
    def swim(self):
        print("swim")

# m=Mammal()
# m.eat()
# print(m.age)

# f=Fish()
# f.swim()


# A Good example of inheritance
class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False
    
    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened=True   
        
    def close(self):
        if self.opened:
            raise InvalidOperationError("Stream is already close.")
        self.opened=False
    
    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")
        
        
class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")
        

stream=Stream()
stream.open