import sys

def merge(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

n = int(sys.stdin.readline())
for _ in range(n):
    p = list(map(int, sys.stdin.readline().split()))
    dp = [[False] * (n+1) for _ in range(2*n)]
    for i in range(2*n):
        if i < n:
            for j in range(i+1):
                if p[i] <= p[j]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        else:
            for j in range(n):
                if p[i] <= p[n+j]:
                    dp[i][n+j] = True
                else:
                    dp[i][n+j] = False
    print("YES" if any(dp[2*n-1][j]) else "NO")
