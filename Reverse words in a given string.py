s = "geeks quiz practice code"

s1 = []

for word in s.split():
    s1.append(word)

low = 0
high = len(s1)-1

while low < high:

    s1[low], s1[high] = s1[high], s1[low]
    low = low+1
    high = high-1

print(s1)