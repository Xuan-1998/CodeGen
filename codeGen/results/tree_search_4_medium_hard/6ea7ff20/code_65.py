def mergeable(p):
    n = len(p) // 2

    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(2*n+1):
        if i < 2:
            continue
        
        left, right = p[:i], p[i:]
        
        for k in range(i//2):
            if dp[k][i//2 - 1] and dp[i//2][i-1]:
                dp[i//2][i-1] = True
                break

    return "YES" if dp[n][n-1] else "NO"


# Read input from stdin
n = int(input())
p = list(map(int, input().split()))

print(mergeable(p))
