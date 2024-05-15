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

prices = list(map(lambda item: item[1], items)) # first method
filtered_prices = (list(map(lambda item: item[1] >= 10, items))) # second method

best_prices = [item[1] for item in items] # <------------------- best method

print(best_prices)