def summ(num1, num2):
    try:
        print(num1/num2)
    except (TypeError, ZeroDivisionError) as err:
        print(err)

while True:
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    print(summ(x, y))

    break


while True:
    try:
        age = int(input('Enter your age: '))
        10/age

        print(f'You are {age} years old')

    except ValueError:
        print('Enter a valid age in number')

    except ZeroDivisionError:
        print('Enter a number greater than zero')

    else:
        print('Done')
        break
