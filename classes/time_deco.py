'''
Lesson 2: Decorator function real life example

To see definition of decorators go to Lesson1 (decorator.py)

ref:https://realpython.com/primer-on-python-decorators/
'''

import functools
from re import I            # remain the name of decorated function
import time
from tracemalloc import start

def timer(func):
    '''Print runtime of the function'''
    @functools.wraps(func)
    def wrap_it(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f'Finished {func.__name__!r} in {run_time:.4f} secs')
        '''by using !r, repr(object).__format__() is used >> ref1'''
        return value
    return wrap_it

@timer
def waste_some_time(num):
    for _ in range(num):
        sum([i**3 * + i for i in range(10000)])

waste_some_time(10)
waste_some_time(100)
waste_some_time(1000)


'''ref1: https://stackoverflow.com/questions/33097143/what-is-the-difference-between-r-and-r-in-python'''