import sys

n, t = map(int, input().split())
fraction = float(input())

grade = int(fraction * (10 ** n))
max_grade = grade

for i in range(n):
    if i > t:
        break
    fraction += 0.5
    grade = int(fraction * (10 ** n))
    max_grade = max(max_grade, grade)

print(max_grade)
