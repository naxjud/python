numbers = [14, 2,3,4,5,6,7,6,5,7,8,8,9,10,11,12,13,14,14]
numbers2 =[]

for number in numbers:
    if number not in numbers2:
        numbers2.append(number)

print(numbers2)