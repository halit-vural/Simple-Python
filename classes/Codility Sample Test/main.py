'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import defaultdict


def solution(A):
    # write your code in Python 3.6
    arr = sorted(A)
    min_num = 1
    for i in arr:
        if min_num == i:
            min_num += 1
    return min_num

ex1 = [1, 3, 6, 4, 1, 2]
ex2 = [234,10,235,2,3344,3,122,4,64,5,23, 9, 64,6,145,7,46324,8, 23234,1]

ex = ex2
num = solution(ex)
print(num)

from collections import defaultdict

def solution2(A):
    d = defaultdict(lambda: False)
    min_num = 1
    for i in A:
        d[i] = True
        if i == min_num:
            min_num += 1
            while d[min_num]:
                min_num += 1
    return min_num

num = solution2(ex)
print(num)
