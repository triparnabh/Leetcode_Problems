import math

class Solution(object):
    def majorityElement(self, nums):

        majority = math.ceil(len(nums) / 2)

        counter = {}

        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        for i in counter:
            if counter[i] > majority:
                return i