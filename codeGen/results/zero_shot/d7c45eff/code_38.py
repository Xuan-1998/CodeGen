import sys

n, k = map(int, input().split())
s = input()

if n >= k:
    if k == 1 or s[k-2] <= s[-1]:
        print(s[:k])
    else:
        print(s[:-1][::-1][:k][::-1])
else:
    print(s)
