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
        self.tags={}
    
    def add(self, tag):
        self.tags[tag.lower()]=self.tags.get(tag.lower(),0)+1
    
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(),0)
    
    def __setitems__(self, tag, count):
        self.tags[tag.lower()]=count
        
    def __len__(self):
        return len(self.tags)
    
    def __iter__(self):
        return iter(self.tags)

cloud=TagCloud()
cloud.add("Python")
cloud.add("python")
# cloud["python"]=10
cloud.add("python")
cloud.add("nabin")
cloud.add("Nabin")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
# cloud=TagCloud()
print(len(cloud))
# cloud["python"]=10 