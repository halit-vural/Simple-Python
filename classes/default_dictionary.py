my_dict = {}
my_dict['one'] = 1 
# print(my_dict['zero'])          # KeyError: 'zero'
# my_dict['infinity'].append(4)       # KeyError: 'infinity'

from collections import defaultdict

def_dict = defaultdict(list)  # set .default_factory to list. use WITHOUT ()
def_dict['one'] = 1  # Add a key-value pair
def_dict['missing']  # Access a missing key returns an empty list
def_dict['another_missing'].append(4)  # Modify a missing key
print(def_dict)


dept = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe')]

dept_dd = defaultdict(list)
for department, employee in dept:
    dept_dd[department].append(employee)

print(dept_dd)

###
dept_d = dict()
for department, employee in dept:
    dept_d.setdefault(department, []).append(employee)

print(dept_d)


dept = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe')]

dept_dd = defaultdict(set)
for department, employee in dept:
    dept_dd[department].add(employee)

dd = defaultdict(int)           # init first item as 0
for department, _ in dept:
    dd[department] += 1
print(dd)

word = 'mississippi'

dd = defaultdict(int)
for letter in word:
    dd[letter] += 1
print(dd)

from collections import Counter
cnt = Counter(word)
print('With Counter() this time:', cnt)


incomes = [('Books', 1250.00),
           ('Books', 1300.00),
           ('Books', 1420.00),
           ('Tutorials', 560.00),
           ('Tutorials', 630.00),
           ('Tutorials', 750.00),
           ('Courses', 2500.00),
           ('Courses', 2430.00),
           ('Courses', 2750.00),]

dd = defaultdict(float)
for product, income in incomes:
    dd[product] += income

for product, income in dd.items():
    print(f'Total income for {product} is ${income:.2f}')







