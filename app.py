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
#message length with len
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


#dictionaries
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
