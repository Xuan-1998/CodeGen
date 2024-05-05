import sys

n, t = map(int, input().split())
fraction = float(input())

max_grade = 0
for i in range(n):
    if (int(1e9 / t)) ** i <= fraction % 10:
        max_grade += 1
    else:
        break

print(max_grade)
