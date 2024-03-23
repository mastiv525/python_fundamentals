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
    print("World!")

basic()