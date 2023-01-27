def sockMerchant(n, ar):
    count_dict = {}
    pairs = 0
    for num in ar:
        count_dict[num] = count_dict.get(num, 0) + 1
        if count_dict[num] == 2:
            pairs += 1
            count_dict[num] = 0
    return pairs
        


N = 9
array = [10, 20, 20, 10, 10, 30, 50, 10, 20]
p = sockMerchant(N, array)
print(p)