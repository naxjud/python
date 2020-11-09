import math

"""name = input("what's your name ")
color = input("favourite color? ")
print("hi "+name+" your favourite color is "+color)
"""

"""
birthyear = input("what's your birth year ")
age = 2020 - int(birthyear)
print(type(age))
print(age)
"""

email = '''
Hi John
here is our Email to you
the support
'''

print(email)

my_text = "python Course for Beginners"
cp_text = my_text[:]

print(my_text[0:3])
print(my_text[3:])
print(my_text[:6])
print(my_text[-1])
print("strings##################")
name = "Moussa"
last = "Zraidi"
message = f'{name} [{last}] is a coder'
print(message)
# message length with len
print(len(message))
print(message.upper())
print(message.lower())
print(message.title())

print(message.find('coder'))
print(message.replace('coder', 'Programmer'))

print('coder' in message)

# integer division
x = 10 // 3
print(x)
# exponent 2^3=8
y = 2 ** 3
print(y)

z = 2.9
print(round(z))
# |f|
f = -5.4
print(abs(f))

print(math.ceil(1.9))
print(math.floor(3.9))

is_hot = False
is_cold = True

if is_hot and not is_cold:
    print("it's a hot day")
    print("Drink plenty of water")
elif is_cold and not is_hot:
    print("It's cold")
    print("wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")

# dictionaries
customer = {
    "name": "john Smith",
    "age": 18,
    "is_verified": True
}

print(customer.get("name"))
print(customer["age"])


def greet_user(first_name, last_name):
    print(f'Hi {first_name}, {last_name}')
    print("i wish you a nice day")


greet_user("john", last_name="Smith")


class Point:
    def __init__(self, x_cord, y_cord):
        self.x = x_cord
        self.y = y_cord

    def move(self):
        print("move")

    def draw(self):
        print(f' x= {self.x}, y={self.y}')


point1 = Point(50, 20)
point1.draw()
print(point1.x)

#dry don't repeat yourself

#inheritance


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass

"""
print("Hello Moussa")
print('o-----')
print('  ||||')
print('*'*10)
"""

name = "prince"
age = 20
is_patient = False

name = 'What ist your name? '


print(name)
print(age)
print(type(is_patient))

for item in range(5, 10, 2):
    print(item)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price

print(f"Total price: {total}")

for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

# 2D lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item)


#list methods
numbers = [5,3,8,5,54]
numbers2 = numbers.copy()
numbers.append(12)
numbers.insert(0, 10)
numbers.remove(54)
# leer machen
# numbers.clear()
numbers.pop()
index = numbers.index(5)
print(numbers)
print(index)
print(50 in numbers)
print(numbers.count(5))

numbers.sort()
numbers.reverse()
print(numbers)

# tupples array not editable
my_tupple = (55, 32, 44)
print(my_tupple[0])


# unpacking
x, y, z = my_tupple
print(x)
print(y)
print(z)

#dictionary
customer = {
    "name": "John smith",
    "age": 30,
    "is_verified": True,
    "birthdate": "10 June 2009"
}

print(customer["name"])
print(customer.get("birthdate","01 Januar 1980"))
