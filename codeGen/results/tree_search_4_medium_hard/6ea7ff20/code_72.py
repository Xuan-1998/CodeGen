import sys

def merge(a, b):
    res = []
    while a and b:
        if a[0] < b[0]:
            res.append(a.pop(0))
        else:
            res.append(b.pop(0))
    return res + a + b

def can_merge(n, p):
    dp = [[False] * (n+1) for _ in range(n+1)]
    dp[0][0] = True
    for i in range(1, n+1):
        for j in range(min(i, n), 0, -1):
            if p[i-1] > p[j-1]:
                if i == j:
                    return "NO"
                dp[i][j] = dp[i-1][j]
            elif p[i-1] < p[j-1]:
                dp[i][j] = dp[i][j-1]
            else:
                for k in range(j, 0, -1):
                    if not (dp[i-1][k-1]):
                        break
                else:
                    return "NO"
    return "YES"

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
print(can_merge(n, p))
