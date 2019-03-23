
def transition_point(nums, N):

    first = nums[0]

    for i in range(1, N):
        if nums[i] == first:
            continue
        else:
            return i
            break


if __name__ == '__main__':

    nums = [0,0,0,1,1]
    N = len(nums)

    answer = transition_point(nums, N)
    print (answer)


