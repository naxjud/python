import random

numbers = [15, 20, 13, 29, 50, 17, 53, 32]

biggest = 0
place = 0

for number in numbers:
    if number > biggest:
        biggest = number

place = numbers.index(biggest) + 1

print(f"the biggest number is {biggest}")
print(f"it's the number {place} in the list")