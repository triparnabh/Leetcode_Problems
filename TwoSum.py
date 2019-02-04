class Solution:
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            nums_new = nums[i + 1:]
            for x in range(len(nums_new)):
                if nums[i] + nums_new[x] == target:
                    return i, x + i + 1