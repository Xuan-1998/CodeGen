import sys

def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    return [b[0]] + merge(a, b[1:])

def solve(n, p):
    dp = [[False] * (2*n) for _ in range(2*n)]

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i + j == 0:
                continue
            if p[i*2] < p[j*2]:
                dp[i][j] = any(dp[k][j-1-k] for k in range(min(i+1, j)))
            elif p[i*2] > p[j*2]:
                dp[i][j] = any(dp[i-1-k][k] for k in range(min(i, j)))
            else:
                if i == 0 or j == 0:
                    continue
                for a_k in range(2*n):
                    b_l = a_k + n - 1
                    if p[a_k] < p[b_l]:
                        dp[i][j] = any(dp[k][j-1-k] for k in range(min(i+1, j)))
                    elif p[a_k] > p[b_l]:
                        dp[i][j] = any(dp[i-1-k][k] for k in range(min(i, j)))
                    else:
                        dp[i][j] = True

    return "YES" if dp[n-1][n-1] else "NO"

# Read input from stdin
n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

print(solve(n, p))
