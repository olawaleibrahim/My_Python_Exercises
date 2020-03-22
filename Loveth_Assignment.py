x = int(input('How many numbers do you want to input? '))
y = input('Input the numbers and separated by space')

nums = y.split(' ')
nums_int = []
for i in nums:
    new = int(i)
    nums_int.append(new)

sum = 0
for i in nums_int:
    sum = sum + i

average = float(sum/x)

print('The sum of the numbers is', sum)
print('The average of the numbers is', average)


