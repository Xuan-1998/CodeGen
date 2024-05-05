import sys

def merge(a, b):
    result = []
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    result.extend(a)
    result.extend(b)
    return result

def solve(n, p):
    dp = [[False for _ in range(2*n+1)] for _ in range(2*n+1)]
    for i in range(2*n+1):
        dp[i][0] = True
        dp[i][i] = (i % 2 == 0)
    
    for i in range(1, 2*n+1):
        for j in range(min(i, 2*n)+1):
            if i - j < 0 or dp[i-j][j]:
                if p[i-1] > p[i-j-1]:
                    dp[i][j] = dp[i-j][j]
                else:
                    dp[i][j] = any(dp[k][min(j, k)] and not (p[i-1] in [pi for pi in range(k)]) for k in range(i-j))
            else:
                if p[i-1] > p[i-j-1]:
                    dp[i][j] = False
                else:
                    dp[i][j] = all(not (p[i-1] in [pi for pi in range(k)]) and dp[k][min(j, k)] for k in range(i-j))
    
    return 'YES' if any(dp[n][k] for k in range(2*n+1)) else 'NO'

n = int(sys.stdin.readline().strip())
p = list(map(int, sys.stdin.readline().strip().split()))
print(solve(n, p))
