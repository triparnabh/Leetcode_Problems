class Solution:
    def longestConsecutive(self, nums) -> int:

        s = set(nums)
        answer = 0
        # n = len(s)

        for value in s:

            if value - 1 not in s:
                j = value
                while (j in s):
                    j = j + 1

                answer = max(answer, j - value)

        return answer