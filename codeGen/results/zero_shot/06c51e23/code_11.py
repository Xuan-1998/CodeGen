import math

def find_max_grade():
    n = int(input())  # length of decimal fraction
    t = int(input())  # time limit
    fraction = input()  # decimal fraction itself

    max_grade = 0  # initialize maximum grade
    for i in range(n):
        digit = int(fraction.split('.')[1][i])  # get the current digit
        if math.floor(10**i * digit) + 1 <= t:  # check if rounding up wouldn't exceed time limit
            max_grade = max(max_grade, digit + 1)  # update maximum grade
        elif math.ceil(10**i * digit) - 1 >= -t:  # check if rounding down wouldn't exceed time limit
            max_grade = max(max_grade, digit)  # update maximum grade

    return int(max_grade)

print(find_max_grade())
