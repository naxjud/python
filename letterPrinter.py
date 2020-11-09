numbers = [2, 2, 2, 2, 5]
my_string = ""

for n in numbers:
    print("x" * n)

for item in numbers:
    my_string = ""
    for count in range(item):
          my_string += "x"
    print(my_string)