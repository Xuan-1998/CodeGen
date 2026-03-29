import sys

n, t = map(int, input().split())
x = float(input())

grade = 0
for i in range(n):
    digit = int((10**i) * (x - int(x)))
    if digit >= 5:
        grade += 1
    x -= digit / (10**i)

print(grade)
