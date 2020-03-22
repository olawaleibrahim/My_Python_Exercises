# Using the map function

from functools import reduce


def raisetopower(lis):
    return lis*2


my_list = (1, 2, 3, 4, 5, 6, 7, 8)
print(raisetopower(my_list))

print(tuple(map(raisetopower, my_list)))
print(my_list)

# Using the zip function

names = ['David Jones', 'Abraham Daniels', 'Richard Crawford']
ages = [23, 45, 19]
hobbies = ['Swimming', 'Dancing', 'Playing']

data = list(zip(names, ages, hobbies))
print(data)
print(data[2])

# Using the filter function


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))

# Using the reduce function

# Exercise
# 1.
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capital(item):
    return item.upper()


print(list(map(capital, my_pets)))

# 2.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
my_numbers.sort()

print(list(zip(my_strings, my_numbers)))

# 3.
scores = [73, 20, 65, 19, 76, 100, 88]


def above_average(item):
    return item >= 50


print(list(filter(above_average, scores)))

# 4.


def combine_all(comb, item):
    print(comb, item)
    return(comb + item)


print(reduce(combine_all, scores, 1))

# Lambda Functions
print(list(map(lambda item: item*item, scores)))

a = [(0, 2), (4, 3), (10, -1), (9, 9)]

a.sort(key=lambda x: x[1])
print(a)

# List Comprehensions
my_list1 = [num*2 for num in range(0, 100) if (num*2) % 3 == 0]
print(my_list1)

# Dictionary Comprehensions
simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

new_dict = {key: value**2 for key, value in simple_dict.items() if value %
            2 == 0}
print(new_dict)

new_dict1 = {num: num**2 for num in range(10)}
print(new_dict1)

# Comprehensions Exercise
some_list = ['o', 'n', 'o', 'm', 'a', 't', 'o', 'p', 'o', 'e', 'i', 'a']

duplicates = []
for i in some_list:
    if some_list.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)

print(duplicates)

duplicates1 = list(set([i for i in some_list if some_list.count(i) != 1]))
print(duplicates1)
