print('hello world')


def summary(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


print(summary(1098, 347))
print(minus(234, 369))

tuple_comp = [i for i in range(0,100) if i%2 == 0]
tuple_comp = tuple(tuple_comp)
print(type(tuple_comp))