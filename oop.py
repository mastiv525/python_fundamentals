
############### CLASSES

# Class: is a blueprint for creating new objects
# Object: is a instance of a class

# our point object need some initial values like x and y
# to set these values we need a CONSTRUCTOR
# __init__ is a magic method and its a CONSTRUCTOR and its executed when we create a new point object
# !! self is a reference to current point object
# we can define attributes later in the code
class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point ({self.x, self.y})")


point = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(5, 6)
point4 = Point(8, 10)

point.draw()
point2.draw()
point3.draw()
point4.draw()

print(point)
print(point == point2)
print(point4 > point3)
print(point2 + point3)

# if you want to make certain attributes or certain methods in the class private use "__"

class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)

cloud = TagCloud()

cloud.add("Python")
cloud.add("python")
cloud.add("python")

print(cloud.tags)
print(len(cloud))
cloud["python"] = 10
for tag in cloud:
    print(tag)

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product = Product(50)
print(product.price)

######## INHERITANCE

# super daje dostep do atrybutów z najwyższej klasy
class Animal:
    def __init__(self):
        print("Amimal Constructor")
        self.age = 14

    def eat(self):
        print("eat")

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 58

    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
m.eat()
print(m.age)
print(m.weight)

from abc import ABC, abstractmethod

class InvalidOperationEror(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationEror("Stream is already opened.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationEror("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Readind data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

class MemoryStream(Stream):
    def read(self):
        print("Read")

stream = MemoryStream()
stream.open()

### Polymorphism

from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

def draw(UIcontrols):
    for control in UIcontrols:
        control.draw()

ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])

class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super(TrackableList, self).append(object)

list_obj = TrackableList()
list_obj.append("1")

# very good to use in classes that have only data and no methods you can use named tuple instead of classes
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)

print(p1 == p2)