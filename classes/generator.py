'''
Any function that has a yield becomes a generator.

https://www.programiz.com/python-programming/generator
'''

def reverse_str(str):
    for i in range(1, len(str)+1):
        yield str[-i]

for c in reverse_str('generator example'):
    print(c, end='')


def fibbonachi(n):
    x, y = 0, 1
    for _ in range(n):
        0,1,1,2,3,5,8,13,21
        x, y = y, x+y
        yield x


print()
for x in fibbonachi(10):
    print(x, end=', ')

def series(n):
    for i in range(n+1):
        yield 2**i

print()
for i in series(10):
    print(i, end='+')


def n3n(n):
    for i in range(1,n+1):
        yield i**3+i

print()
for i in n3n(10):
    print(i, end='+')



# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)

print()
print(list_)
for i in generator:
    print(i, end=', ')
