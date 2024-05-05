import sys

n, k = map(int, input().split())
s = input()

if n > k:
    print(s[:k])
else:
    if s[k-1] <= chr(122):  # 'z' is the last lowercase letter
        print(s)
    else:
        for _ in range(k-n):
            print(s + s[-1], end='')
