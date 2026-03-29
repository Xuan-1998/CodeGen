import sys

n, k = map(int, input().split())
s = input()

if k >= n:
    print(s * (k // n))
else:
    if s[k-1] <= s[0]:
        print(s[:k])
    else:
        print(s + s[:k-1])
