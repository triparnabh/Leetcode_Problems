odd = []
even = []
result =[]


def two_way_sort(arr, arr_len):

    for i in arr:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)

    even.sort()
    odd.sort(reverse=True)

    result = odd + even
    return result



arr_len = 6
arr = [1, 3, 2, 7, 5, 4]
result = two_way_sort(arr, arr_len)
print(result)
