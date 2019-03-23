
def count_X(num, lower, upper):
    count = 0

    for i in range(lower+1, upper-1):
        if str(num) in str(i):
            count+=1
    return count


if __name__ == '__main__':

    num = 5
    upper= 250
    lower = 100

    answer = count_X(num, lower,upper)
    print (answer)


