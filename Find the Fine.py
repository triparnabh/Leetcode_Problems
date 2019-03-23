def totFine(car_num, n, date, fine):

    odd = []
    even = []
    total_fine = 0

    for i in car_num:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)

    if date % 2 == 0:
        for car in odd:
            total_fine+=250
    else:
        for car in even:
            total_fine+= 250

    return total_fine



if __name__ == "__main__":
    car_num = [3, 4, 1, 2, 9,13,7,24,25,31]
    n = len(car_num)
    date, fine = 12, 250

    # function calling
    print(totFine(car_num, n, date, fine))



