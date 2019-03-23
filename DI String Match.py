class Solution:
    def diStringMatch(self, S:'str') -> 'List[int]':

        temp = []
        low = 0
        N = len(S)
        high = N

        for char in S:
            if char == "I":
                temp.append(low)
                low = low + 1
            else:
                temp.append(high)
                high = high - 1

        temp.append(high)
        return temp
