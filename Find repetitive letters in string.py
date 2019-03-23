s = "geeksforgeeks"

di ={}

for i in s:
    if i in di:
        di[i]+=1
    else:
        di[i] = 1

for i in di:
    if di[i]>1:
        print(i)