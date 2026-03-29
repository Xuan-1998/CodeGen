import sys
n, k = map(int, input().split())
s = input()

if k > n:
    result = s * (k // n) + 'a' * (k % n)
elif k == n:
    result = s
else:
    if s[-1] <= 'a':
        result = s[:-1]
    else:
        result = s + s[:k-1]
print(result)
