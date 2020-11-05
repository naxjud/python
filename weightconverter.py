import math
weight = int(input("Your Weight: "))
unit = input("L(bs) or K(g): ")
convert = 0

if unit.lower() == 'k':
    convert = weight / 0.45
    print(f'Your Weight is {convert} Lbs')
elif unit.lower() == 'l':
    convert = weight * 0.45
    print(f'Your Weight is {convert} kg')
else:
    print('something went wrong')

