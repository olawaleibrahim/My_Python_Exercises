dicts = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
  'x': 24, 'y': 25, 'z': 26}

your_input = input('Input your name here: ')
print(your_input)
numeric_value = []
for i in your_input:
    numeric_value.append(dicts[i])

true_value = 0
for j in numeric_value:
    true_value += j

print(numeric_value)
print('This is the value of your name', true_value)
