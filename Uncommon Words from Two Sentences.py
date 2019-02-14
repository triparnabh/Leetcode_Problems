class Solution:
    def uncommonFromSentences(self, A: 'str', B: 'str') -> 'List[str]':

        word_di = {}
        output = []

        for word in A.split():
            if word in word_di:
                word_di[word] += 1
            else:
                word_di[word] = 1

        for word in B.split():
            if word in word_di:
                word_di[word] += 1
            else:
                word_di[word] = 1

        for word in word_di:
            if word_di[word] == 1:
                output.append(word)

        return output

