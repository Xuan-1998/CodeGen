import sys

n = int(sys.stdin.readline())
t = int(sys.stdin.readline())

decimal_fraction = sys.stdin.readline().rstrip()

max_grade = 0
for i in range(n):
    digit = int(str(decimal_fraction)[i + 1])
    if digit >= 5:  # round up if the digit is 5 or greater
        max_grade += 1
    else:
        max_grade += 0.5

print(int(max_grade))
