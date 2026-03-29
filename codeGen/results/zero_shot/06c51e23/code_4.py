import math

n = int(input())  # length of decimal fraction
t = int(input())  # time limit
frac_str = input()  # decimal fraction as a string

max_grade = 0  # maximum grade obtained so far

for i in range(n - 1, -1, -1):
    digit = int(frac_str[i])
    if digit >= 5:
        max_grade += 1
    else:
        break

print(max_grade)
