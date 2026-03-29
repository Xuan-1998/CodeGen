import sys
n, k = map(int, input().split())
s = input()

if k >= n:
    if s[k-1] <= s[0]:
        result = s[:k]
    else:
        result = s + s[:k-n]
else:
    if k % 2 == 0 and s[k//2-1] <= s[0]:
        result = s[:k]
    elif k % 2 != 0 and s[(k+1)//2-1] <= s[0]:
        result = s[:k]
    else:
        result = s + s[:k-n]

print(result)
