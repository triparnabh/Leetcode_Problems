

nums = [1, 2, 4, 3, 3, 2, 5, 6, 1, 6, 5]
count = {}

for key in nums:
    if key in count:
        count[key]+= 1
    else:
        count[key] =1

for key in count:
    if count[key]==1:
        print(key)