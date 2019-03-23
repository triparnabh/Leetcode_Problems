
def transition_point(number, money):

    if number % 2 == 0:
        count = number //2
        max_money = count * money
    else:
        count = (number//2) +1
        max_money = count * money

    return max_money


if __name__ == '__main__':

    number= 2
    money = 12


    answer = transition_point(number,money)
    print (answer)


