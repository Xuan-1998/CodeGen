import sys

# Read input from stdin
n = int(input())
t = int(input())
decimal_fraction = float(input())

grade = 0
for i in range(n):
    if t > 1:  # If we have enough time, round the current digit
        grade += (int(str(decimal_fraction).split('.')[1][i]) + 1) // 2
        t -= 1
    else:
        break

print(grade)
