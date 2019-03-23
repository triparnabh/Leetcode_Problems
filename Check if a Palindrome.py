s = "MALAYALAM"

low = 0
high = len(s)-1

while low < high:
    if s[low] == s[high]:
        low+=1
        high-=1
print("True")

