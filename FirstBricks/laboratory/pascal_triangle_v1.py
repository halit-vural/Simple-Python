'''
pascal_triangle v1
@author: Halit Vural

Can you print Pascal's Triangle with variables?

'''

'''
Solution:

Pascal triangle:
         1
        1 1
       1 2 1
      1 3 3 1
     1 4 6 4 1
    1 5 10 10 5 1
    
The very first version:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1


columns as variables:
a b c d e f
1 0 0 0 0 0
1 1 0 0 0 0
1 2 1 0 0 0
1 3 3 1 0 0
1 4 6 4 1 0
1 5 10 10 5 1   

'''


a = 1
b = c = d = e = f = 0

print(a)
b = b + a
print(a, b)
c = c + b
b = b + a
print(a,b,c)
d = d + c
c = c + b
b = b + a
print(a,b,c,d)
e = e + d
d = d + c
c = c + b
b = b + a
print(a,b,c,d,e)
f = f + e
e = e + d
d = d + c
c = c + b
b = b + a
print(a,b,c,d,e,f)
# g = g + f
# f = f + e
# e = e + d
# d = d + c
# c = c + b
# b = b + a
# print(a,b,c,d,e,f,g)


# second stage ##########
'''
 Let's try to give it's shape:


         1
        1 1
       1 2 1
      1 3 3 1
     1 4 6 4 1
    1 5 10 10 5 1
    
'''

a = 1
b = c = d = e = f = 0
space = ' '

times = 5
print(space * times,a)
b = b + a
times = 4
print(space * times,a, b)
c = c + b
b = b + a
times = 3
print(space * times,a,b,c)
d = d + c
c = c + b
b = b + a
times = 2
print(space * times,a,b,c,d)
e = e + d
d = d + c
c = c + b
b = b + a
times = 1
print(space * times,a,b,c,d,e)
f = f + e
e = e + d
d = d + c
c = c + b
b = b + a
times = 0
print(space * times,a,b,c,d,e,f)





