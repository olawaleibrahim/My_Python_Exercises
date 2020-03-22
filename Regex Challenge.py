sentence = '''57. He likes a lot of coding. 
All what you are seeing is not real 
How will you feel if your code controls the world? 
Money is the machine gun we don’t like seeing bugs and so we crush them'''

print(sentence)

new = sentence.split(' ')
print(type(new))

new1 = new[::-1]

print(new1)

reverse = ''
for i in new1:
    reverse = reverse + ' ' + i

print(reverse)

print(sentence[::-1])


# CHALLENGE TWO
input = [[5],
         [3, 2],
         [1, 2, 3],
         [5, 2],
         [3, 7, 5, 9, 2],
         [6, 4],
         [4, 9, 10, 4, 2, 5],
         [10, 3],
         [6, 3, 2, 14, 2, 10, 11, 4, 12, 13],
         [10, 2],
         [6, 3, 2, 14, 2, 10, 11, 4, 12, 13]]

for row in input:
    print(f'The max value is {max(row)} and the minimum is {min(row)}')

# CHALLENGE THREE

array = [[5],
         [2],
         [11101241332150],
         [3],
         [123432211],
         [63010],
         [116940],
         [1],
         [48901203410128],
         [4],
         [90440232110002425821],
         [10392311110],
         [32905031],
         [40352156931154159],
         [3],
         [680203110301],
         [403021534153100],
         [20217]]
# code to extract the zeros and ones fromeach list in the array

for row in array:
    for i in row:

        if i != 0 or i != 1:
            row.pop(i)
            
