from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'The time it took is {t2-t1}')
        return result
    return wrapper

@performance
def long_time():
    for i in range(10000000):
        i*5


#print(long_time())

with open('script.py', mode='r+') as my_script:
    print(my_script.write(''))
    print('script.py')