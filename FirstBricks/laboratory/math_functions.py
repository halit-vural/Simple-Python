import math

number = 3.14
result = math.ceil(number)
print(number, 'ceil', result)

number = 3.99
result = math.floor(number)
print(number, 'floor', result)


number = 3.5
result = round(number)
print(number, 'round', result)


x, y = 9, 12
result = math.gcd(x,y)
print(x,y, 'gcd', result)


x, y = 17, 23
result = math.gcd(x,y)
print(x,y, 'gcd', result)

x, y = 18, 15
result = math.gcd(x,y)
print(x,y, 'gcd', result)


print(math.pi)
print(round(math.pi, 3))


x, y = 12, 9
result = math.fmod(x,y)
print(x,y, 'modulus', result)



x, y = 17, 9
result = math.fmod(x,y)
print(x,y, 'modulus', result)


x, y = 12, 9
result = x % y
print(x,y, '%', result)

