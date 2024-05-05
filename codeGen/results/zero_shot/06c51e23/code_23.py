import sys

def max_grade(n, t, fraction):
    if n == 0:  # base case: no more digits to round
        return int(fraction * (10 ** t))  # convert fraction to integer and scale by time limit
    else:
        max_grade = 0
        for i in range(1, 11):  # consider all possible rounding positions (0.01 to 0.09)
            rounded_fraction = round(float('%.{}f'.format(i) % fraction), i - 1)  # round the fraction at position i
            grade = int(rounded_fraction * (10 ** t))  # calculate the grade for the rounded fraction
            max_grade = max(max_grade, grade)  # update the maximum grade
        return max_grade

n, t = map(int, input().split())  # read n and t from stdin
fraction = float(input())  # read the decimal fraction from stdin

print(max_grade(n, t, fraction))  # print the maximum possible grade
