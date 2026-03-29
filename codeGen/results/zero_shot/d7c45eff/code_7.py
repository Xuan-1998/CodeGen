import sys

n, k = map(int, input().split())
s = input()

if k == n:
    print(s)
elif k > n:
    print(s * (k // n))
else:
    print(s[:k])
