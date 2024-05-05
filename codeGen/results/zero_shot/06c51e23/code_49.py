import sys
n, t = map(int, input().split())
fraction = float(input())
grade = 0
i = 1
while i <= n:
    if i > t: break
    grade += int((10**i) * (10**(t-i+1)) - 5)
    i *= 10
print(grade)
