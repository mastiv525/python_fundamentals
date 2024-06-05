import math

students_count = 100
rating = 4.99
is_okay = True

random_name = "Barad dur"
new_name = "this city will be a \"Minas Durum\" now"
title = "Lord of the Rings"

print(students_count)
print(len(random_name))


print(random_name[0])
print(random_name[0:3])
print(random_name[3:9])
print(random_name[-2])
print(new_name)
print(f"{random_name} {new_name}")
print(title.capitalize())
print(title.lower())
print(title.upper())
print(title.find("the"))
print(title.replace("R", "B"))
print("of" in title)
print("ok" not in title)


print(round(2.9))
print(abs(-2.9))
print(math.ceil(23.5))


temperature = 15

if temperature > 30:
    print("it's warm")
    print("drink water")
elif temperature > 20:
    print("it's nice")
else:
    print("it's cold")

#ternary operator

age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
print(message)

#logical operators

high_income = False
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

#chaining comparison

age = 22
if age >= 18 and age <65:
# if 1 <= age < 65:     <- much better
    print(f"Eligible \n")

# for loops
for number in range(1, 4):
    print("Attempt", number, number * ".")

for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# for else loops

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed\n")

# nested loops

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# iterables

for x in "\nPython\n":
    print(x)

for x in [1, 2, 4, 6, 8, 15]:
    print(x)

# while loops

number = 100
while number > 0:
    print(number)
    number //=2

# command = ""
# while command != "quit":
#     command = input(">")
#     print("Echo", command)
#
# # infinite loops
#
# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

# exercise display even numbers

for x in range(1, 10):
    if x % 2 == 0:
        print(x)

# FUNCTIONS

def basic():
    print("Hello")
    print("World!\n")

basic()

def example(first_name, last_name):
    print(f"Hi {first_name} {last_name}\nWelcome aboard!")

example("Alan", "Lekki")

def better_example(first_name, last_name):
    return f"Hi {first_name}{last_name}"

future = better_example("Alan", "Lekki")
# this function is much better for future usage, because we return not print which is easier

def increment(number, by):
    return number + by

print(increment(2, 1))
print(increment(2, by=2))

# def increment_v2(number, by=2):
#     return number + by
# print(increment(2))

# x number of arg

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2 ,3 , 4, 5))

# multiple x key value pairs arguments because of **
def save_user(**user):
    print(user)
    print(user["name"])
save_user(id=1, name="Alan", age=22)


# DATA STRUCTURES

letters = ['a', 'b', 'c']
matrix = [[0, 1], [0, 1]]
zeros = [0] * 5

print(letters)
print(matrix)
print(zeros)

combined = zeros + letters

print(combined)

numb = list(range(20))
print(numb)

chars = list("Hello World")
print(chars)

print(len(numb))
print(len(chars))
print(" ")

# accessing items

numbers = list(range(20))

print(numbers[0:3])
print(numbers[::2])
print(numbers[::-1])
print(" ")

#list unpacking

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, second, third, *other = numbers
print(first, second, third)
print(f'{other}\n')

for index, numbers in enumerate(numbers):
    print(index, letters)

#adding items

letters.append("d")
letters.insert(0, "z")
print(f'{letters}\n')

#removing

letters.pop(0)
letters.append("b")
print(letters)
letters.remove("b")
print(letters)
del letters[0:3]
print(letters)
letters.clear()
print(letters)

#sorting lists

numbers = [10, 5, 79, 741, 226]

print(numbers.sort())
print(numbers.sort(reverse=True))
#better
print(sorted(numbers))
print(sorted(numbers, reverse=True))

items = [
    ("Product", 10),
    ("Product", 9),
    ("Product", 12)
]
def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)

#lambdas key=lambda parameters:expression

items.sort(key=lambda item:item[1])
print(items)

#<- this is a shorter and cleaner way to define a function that we're going to use only once as an argument to another function

prices = list(map(lambda item: item[1], items))
print(prices)

# above, map function takes a lambda functionand appies it to every item of this iterable


#another scenario -> filter function

filtered_prices = list(filter(lambda item: item[1] >=10, items))
print(filtered_prices)

prices = list(map(lambda item: item[1], items)) # basic method
filtered_prices = (list(map(lambda item: item[1] >= 10, items))) # basic method

best_prices = [item[1] for item in items] # <------------------- best method
best_filtered_prices = [item for item in items if item[1] >= 10]  # <------------------- best method

print(best_prices)
print(best_filtered_prices)

### zip function

list1 = [1, 2, 3]
list2 = [10, 20, 30]

#combine two list where all items are tuples
print(list(zip(list1, list2)))
#important
print(list(zip("abc", list1, list2)))

### stacks      LIFO Last In - First Out
# we can use list object as a stack

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
browsing_session.pop() #removing last item in stack
if not browsing_session:
    browsing_session[-1] #get the item on top of the stack

### queues      FIFO First In - First Out

from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
#removing intem from beggining
queue.popleft()

###closer look at tuples
#tuple is READ ONLY LIST and we can use it to contain a sequence of objects but cannot modify

point = (1, 2) + (3, 4)
point_v2 = (1, 2) * 3

print(point)
print(point_v2)

#converting list to tuple
point = tuple([1, 2])
point_v2 = tuple("Hello World")

### swaping variables

x = 10
y = 12
## basic method
# z = x
# x = y
# y = z
## best method

x, y = y, x
print(x, y)

### closer look at arrays and sets

from array import array

numbers = array("i", [1, 2, 3]) #https://docs.python.org/3/library/array.html
# numbers.append()
# numbers.pop()
# numbers.insert()
# numbers.remove()

# set is collection with no duplicates

first_numbers = [1, 1, 1, 2, 2, 3, 3, 3, 3]
uniques = set(first_numbers)
print(uniques)

second_numbers = {1, 4, 8}
second_numbers.add(5)
second_numbers.remove(5)
print(second_numbers)
print(len(second_numbers))

print(uniques | second_numbers) #this will return new set that includes all the items that are either in the first or in the second set
print(uniques & second_numbers) #this will return new set that includes all the items that are both in first and second sets
print(uniques - second_numbers) #this will return new set that includes all the items that are diffrent in this two sets
print(uniques ^ second_numbers) #this will return new set that includes all the items that are either in the first or in the second set but not in the both

# sets are an unordered collection so we cannot acces them using index

####        DICTIONARIES

# dictionary is a collection of key value pairs that we use to map a key to value map - > przypisanie kluczowi wartości tak jak ksiazka adesowa
# in python we can only use immutable types for the keys, value no limitations

point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
# methods to eliminate error
if "a" in point:
    print(point["a"])

print(point.get("a", 0))

del point["x"]
print(point)

# iterations over dicts

for key in point:
    print(key, point[key])

for x in point.items():
    print(x)

for key, value in point.items():
    print(key, value)

# dictionary comperhensions

#example

values = []
for i in range(5):
    values.append(x * 2)

print(values)
# rewrite this to list comperhesion

# [expression for item in items]

values = [x * 2 for x in range(5)]

#and change to dictionary comprehension

values = {x: x * 2 for x in range(5)}
print(values)

### Generator Expressions -> they generate a new value in each iteration

from sys import getsizeof

values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values), "bytes of memory in usage")

values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values), "bytes of memory in usage")

# in situations when we dealing with a really large data set use generetor expession
# which means ( ) brackets

### Unpacking Operator

numbers = [1, 2, 3]

print(*numbers) # exect same output
print(1, 2, 3) # exect same output

## cool tricks

values = list(range(5))
values = [*range(5), *"Hello"]
print(values)
# unpacking lists and strings
first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(*values)
# unpacking dictionaries
first = {"x": 1} # cool way to combine 2 dicts
second = {"x": 10, "y": 2} # cool way to combine 2 dicts
combined = {**first, **second, "z": 1} # cool way to combine 2 dicts
print(combined)

# very important exercise
sentence = "This is a common interview question"

char_list = {}

for i in sentence:
    if i in char_list:
        char_list[i] += 1
    else:
        char_list[i] = 1
print(char_list)

print(sorted(char_list.items(), key=lambda kv:kv[1], reverse=True))

#### EXCEPTIONS

try:
    #age = int(input("\nEnter your age: "))
except ValueError as ex:
    print("You didn't enter a valid age")
    print(ex)
    print(type(ex))
else:
    print("no exeptions were thrown")
print("Execution continues")

# upgrade

try:
    file = open("C:/Users/Alan/Desktop/mosh/main.py")
    #age = int(input("\nEnter your age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age")
else:
    print("No exeptions were thrown")
finally:
    file.close()

# raising exceptions

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("\nAge cannot be 0 or less")
    return 10 / age

try:
    calculate_xfactor(-5)
except ValueError as error:
    print(error)