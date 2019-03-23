
def transition_point(nums):
    sorted_nums = list(sorted(nums))
    difference = []

    for i in range(1, len(sorted_nums)):
        for j in range(i+1, len(sorted_nums)):
            difference.append(sorted_nums[j] - sorted_nums[i])
    return min(difference)




if __name__ == '__main__':

    nums= [87, 32, 99, 75, 56, 43, 21, 10, 68, 49]

    answer = transition_point (nums)
    print (answer)


