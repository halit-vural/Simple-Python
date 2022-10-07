# This program says hello and asks for my name.

print('Hello, world!')
print('What is your name?')    # ask for their name
myName = input()
print('It is good to meet you, ' + myName)

print('What is your age?')    # ask for their age
myAge = input()
year = 2022 - int(myAge)
print('If your age is ', myAge, ', I think your birth year is ', str(year), '?')
