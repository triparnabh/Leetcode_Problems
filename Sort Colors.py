def sortColors(nums):
    zero_count = 0
    one_count = 0
    two_count = 0

    for i in nums:
        if i == 0:
            zero_count += 1
        elif i == 1:
            one_count += 1
        else:
            two_count += 1

    print(zero_count)

    del nums[:]
    print (nums)

    nums += zero_count * [0]
    nums += one_count * [1]
    nums += two_count * [2]

    print(nums)




def main():

    my_Input = [2, 0, 2, 1, 1, 0]
    sortColors(my_Input)


main()