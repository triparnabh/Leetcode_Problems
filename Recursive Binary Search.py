def BinarySearch_Recursive(nums, num_to_find, left, right):

    if right>left:

        mid = (right+left)//2

        if nums[mid] == num_to_find:
            return mid

        elif num_to_find < nums[mid]:
            return BinarySearch_Recursive(nums, num_to_find, left, mid-1)

        else:
            return BinarySearch_Recursive(nums, num_to_find, mid+1, right)

    else:
        return -1


def main():

    nums = [3,4,5,6,7,8,9]
    num_to_find = 4

    result = BinarySearch_Recursive(nums, num_to_find, 0, len(nums)-1)

    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")


main()