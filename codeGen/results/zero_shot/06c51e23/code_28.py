import sys

n, t = map(int, input().split())
frac = float(input())

max_grade = 0
for i in range(n):
    digit = int((10 ** (n - i - 1)) * (frac - int(frac)))

    if digit < 5:
        max_grade += 1
    else:
        max_grade += 0.5

print(int(max_grade))
