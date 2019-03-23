s = 'abcdabgfa'

count = {}

for char in s:
    if char not in count:
         count[char] = 1
    else:
        count[char] = count[char]+ 1

print(count)

for key in count:
    if count[key] >1:
        print (key)