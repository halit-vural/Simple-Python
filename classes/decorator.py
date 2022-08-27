'''
ref: https://realpython.com/primer-on-python-decorators/

Lesson2 >> time_deco.py
'''

import functools        # to remain the original name of the function


def deco_func(func):
    @functools.wraps(func)
    def wrap_up(*args, **kwargs):
        return func(*args, **kwargs) + args[0]  # be sure to include this line for a return
    return wrap_up

@deco_func
def calculate(n):
    return n * n * n

num = 2
print('n =', num, 'formula result:', calculate(num))
print('-'*30)

for i in range(10):
    print('n =', i, 'formula result:', calculate(i))



'''
def deco_func(func, n):
    def wrap_up(n):
        return func(n) + n
    return wrap_up

def calculate(n):
    return n * n * n

num = 3
result = deco_func(calculate, num)

n = 2
print('n =', n, 'formula result:', result(n))
print('-'*30)

for i in range(10):
    print('n =', i, 'formula result:', result(i))


'''



# MORE

'''
from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)
'''