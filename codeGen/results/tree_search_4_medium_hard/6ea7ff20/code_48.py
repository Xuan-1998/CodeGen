import sys

def merge(a, b):
    if not a:
        return b
    elif not b:
        return a
    
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

def can_merge(n):
    p = list(map(int, input().split()))
    dp = [[False] * (2 * n) for _ in range(2 * n)]

    for i in range(2 * n - 1, -1, -1):
        for j in range(i + 1):
            if i == j or (dp[i-1][j-1] and p[i] != p[j]):
                dp[i][j] = True
            else:
                dp[i][j] = False

    a = [None] * n
    b = [None] * n
    for i in range(n):
        if not any(a):
            j, k = 0, 2*n-1
            while j < k and not p[j]:
                j += 1
            while j <= k and not p[k]:
                k -= 1
            a[i], b[i] = p[j], p[k]
        else:
            j, k = n-1, 2*n-1
            while j >= 0 and not p[j]:
                j -= 1
            while k > 0 and not p[k]:
                k -= 1
            a[i], b[i] = p[j], p[k]

    if merge(a, b) == list(p):
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    print(can_merge(n))
