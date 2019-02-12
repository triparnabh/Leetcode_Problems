
def RotateArray(lists, num):
    temp = []

    for item in range(len(lists) - num, len(lists)):
        temp.append(lists[item])

    for item in range(0, len(lists) - num):
        temp.append(lists[item])

    return temp

rotate_num = 3
list_1 = [1, 2, 3, 4, 5, 6]

print(RotateArray(list_1, rotate_num))


# n = 3
#
# list_1 = [1, 2, 3, 4, 5, 6]
# list_1 = (list_1[-n:] + list_1[:-n])
#
# print(list_1)