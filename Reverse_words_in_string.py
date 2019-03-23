class Solution:
    def reverseWords(self, s: str) -> str:

        answer = []

        for i in s.split(" "):
            answer.append(i)
        while '' in answer:
            answer.remove('')

        low = 0
        high = len(answer) - 1

        while low < high:
            answer[low], answer[high] = answer[high], answer[low]
            low += 1
            high -= 1

        return ' '.join(answer)