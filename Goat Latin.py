class Solution:
    def toGoatLatin(self, S: 'str') -> 'str':

        vowels = ['a', 'e', 'i', 'o', 'u']
        trip = 'ma'
        result = []

        for i, word in enumerate(S.split()):
            if word[0].lower() in vowels:
                result.append(word + trip + 'a' * (i + 1))

            else:
                result.append(word[1:] + word[:1] + trip + 'a' * (i + 1))

        str1 = ' '.join(str(e) for e in result)
        return str1

