import math

def floorsqrt(n):

    answer = math.sqrt(n)
    if isinstance(answer, int) == True:
        return answer
    else:
        return math.floor(answer)


def main():

    n = 235

    result= floorsqrt(n)
    print(result)


main()
