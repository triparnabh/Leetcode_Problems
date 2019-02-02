class Solution:

    def removeDuplicates(self, nums):

        if len(nums) < 2:
            return len(nums)

        previous = 0
        for current in range(1, len(nums)):
            if nums[previous] != nums[current]:
                previous += 1
                nums[previous] = nums[current]

        return previous + 1

