
def findMedian(arr):
    arr = sorted(arr)
    idx = len(arr)//2
    return arr[idx]



array = [5,3,1,2,4]
m = findMedian(array)
print(m)