class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target in nums:
            return nums.index(target)
        if len(nums) == 1:
            if nums[0] > target:
                return 0
            else:
                return 1
        else:
            for index, number in enumerate(nums):
                next_index = index + 1
                if next_index < len(nums):
                    if target > nums[index] and target > nums[next_index]:
                        continue
                    elif target > nums[index] and target < nums[next_index]:
                        return next_index
                    elif target < nums[index]:
                        return index
                else:
                    return index + 1