import operator

def topKFrequent(nums, k):
    counter = {}
    answer = []
    c = 1

    for i in nums:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    sorted_x = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)

    print (sorted_x)

    for x in sorted_x:
        if c<=k:
            answer.append(x[0])
            c+=1
    print(answer)



    # for i in range(0, k - 1):
    #     answer.append(sorted_x[i])
    # return answer


def main():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    topKFrequent(nums, k)

main()