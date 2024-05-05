import sys

def alien_language(n, m):
    mod = 10**9 + 7
    res = 1
    for i in range(m):
        if i < n//2:
            res = (res * n) % mod
        elif n//2 <= i < n:
            res = (res * (n-1)) % mod
        else:
            res = (res * 1) % mod
    return res

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(alien_language(n, m))
