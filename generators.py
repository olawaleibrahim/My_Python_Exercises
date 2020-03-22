def generate(num, num1):
    for i in range(num, num1):
        yield i


g = generate(5, 100)
next(g)
next(g)
next(g)
print(next(g))
print(g)

def fib(num):
    sum = 0
    for i in range(0, num):
        if i < num:
            sum = sum + i
            print(sum)

fib(20)