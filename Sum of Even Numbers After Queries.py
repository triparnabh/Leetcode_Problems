class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':

        temp = []

        for i in queries:
            abc = 0
            index = i[1]
            sum = A[index] + i[0]
            A[index] = sum
            for num in A:
                if num % 2 == 0:
                    abc += num
            temp.append(abc)

        return temp







