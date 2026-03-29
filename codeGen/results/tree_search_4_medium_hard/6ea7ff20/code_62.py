import sys

def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

def has_pair_permutation(n, p):
    dp = [[[] for _ in range(n+1)] for _ in range(2*n+1)]

    # Base case
    for j in range(n+1):
        if not j:
            dp[0][j] = [[]]
        else:
            dp[0][j] = [[p[i-1]] for i in range(j, 2*n+1)]

    for i in range(1, 2*n+1):
        for j in range(n+1):
            if not j:
                if p[i-1] < p[i-j]:
                    dp[i][j] = [a + b for a in dp[i-j][j], b in [[p[k-1]] for k in range(j, i)]]
                else:
                    dp[i][j] = [b + a for a in dp[i-j][j], b in [[p[k-1]] for k in range(j, i)]]
            else:
                if p[i-1] < p[i-j]:
                    dp[i][j] = [(a+b) for a in dp[i-j][j-1], b in dp[j-1][n]]
                else:
                    dp[i][j] = [(b+a) for a in dp[i-j][j-1], b in dp[j-1][n]]

    return 'YES' if [[p[0]] + [p[k+1]-k-1] for k in range(n)] in dp[-1][-1] else 'NO'

# Read input from stdin
n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

print(has_pair_permutation(n, p))
