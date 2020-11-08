import math
import converters
from converters import kg_to_lbs
from converters import lbs_to_kg
from utils import find_max

weight = int(input("Your Weight: "))
unit = input("L(bs) or K(g): ")
convert = 0

if unit.lower() == 'k':
    convert = converters.kg_to_lbs(weight)
    print(f'Your Weight is {convert} Lbs')
elif unit.lower() == 'l':
    convert = lbs_to_kg(weight)
    print(f'Your Weight is {convert} kg')
else:
    print('something went wrong')

my_list = [4, 32, 100, 112, 21, 43]

print(find_max(my_list))
