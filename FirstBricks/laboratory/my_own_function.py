
def print_lyrics():
	print ("I'm a lumberjack, and I'm okay.")
	print ("I sleep all night and I work all day.")

def print_space():
	print()
	print()


print_lyrics()
print_space()

def print_lyrics_twice():
	print_lyrics()
	print()
	print_lyrics()
	
	
print_lyrics_twice()
print_space()


def greet_user():
	print('Enter your name:', end='')
	name = input()
	print('Hello ', name, '! How are you.')
	

greet_user()
print_space()



def get_user_name():
	print('Enter your name:', end='')
	name = input()
	return name
	
def get_user_age():
	print('Enter your age:', end='')
	age = int(input())
	return age
	
def greet_user(name, age):
	if age > 7 and age < 15:
		print('Hello ', name, '. How is your school?')

	if age < 7:
		print('Hellooo ', name, '!')



user = get_user_name() # get user name 
years_old = get_user_age()
greet_user(user, years_old)



import math

def circle_circumference(radius):
	return 2 * math.pi * radius
	
	
def circle_area(r):
	return math.pi * r * r
	


print(circle_circumference(2))
print(circle_area(2))


print(circle_circumference(3))
print(circle_area(3))
