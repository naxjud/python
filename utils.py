# import only system from os
from os import system, name


# get the biggest number from a list
def find_max(my_list):
    max_num = my_list[0]

    for number in my_list:
        if number > max_num:
            max_num = number

    return max_num


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


