def findDisappearedNumbers(nums):
    #sorted_nums = nums.sort()
    answer = []

    for i in range(1, len(nums) + 1):
        if i not in nums:
            answer.append(i)
            i += 1
    return answer



def main():

    nums = [1,1]

    abc = findDisappearedNumbers(nums)
    print(abc)


main()