import collections
from collections import Counter

class Solution(object):
    def commonChars(self, A):

        c = collections.Counter(A[0])
        for i in range(1, len(A)):
            c &= collections.Counter(A[i])
        return list(c.elements())

