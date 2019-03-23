
def sortedSquares(A):

    temp = []

    for num in A:
        temp.append(num *num)

    print(temp)
    answer = sorted(temp)
    print(answer)


def main():

    input = [-4,-1,0,3,10]
    sortedSquares(input)


main()