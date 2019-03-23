
def sort012(arr, n):

    count0 = 0
    count1 = 0
    count2 = 0
    result = []

    for i in arr:
        if arr[i] == 0:
            count0 += 1
        elif arr[i] == 1:
            count1 += 1
        else:
            count2 += 1

    for i in range(0, count0):
        result.append(0)
    for i in range(count0+1, count1):
        result.append(1)
    for i in range(count1+1, n):
        result.append(2)
    return result



arr = [ 0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1 ]
n = len(arr)
print(sort012(arr, n))


# time complexity = O(n)
