import math
radius = [1,2,3]
area = list(map(lambda x: round(math.pi*(x**2), 2), radius))
print(area)
# >>> [3.14, 12.57, 28.27]


# edge measures of rectangles
# rectangles = [[1,2],[2,4],[2,6]]

# print(list(lambda x: row[1] for row in rectangles))

# rect_area = list(map(lambda x, y: x * y, ( row[1] for row in rectangles)))
# print(rect_area)


name = 'laptop'
nameTwo = 'laptop'

print(name==nameTwo)
