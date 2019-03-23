"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
find the duplicate one. Example: Input: [1,3,4,2,2] , Output: 2
"""


class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':

        temp = []

        for i in nums:
            if i in temp:
                return i
            else:
                temp.append(i)

