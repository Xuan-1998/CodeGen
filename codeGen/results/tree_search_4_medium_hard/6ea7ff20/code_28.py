def solve(n):
    p = [int(x) for x in input().split()]
    
    dp = [[False] * (n+1) for _ in range(n+1)]
    
    # Initialization
    if not any(p):
        dp[0][0] = True
    
    # Filling the table
    for i in range(1, n+1):
        for j in range(1, n+1):
            if p[i+j-1] in p[:i] or p[i+j-1] in p[i:]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = False
    
    return "YES" if dp[n][0] else "NO"

# Read input and print the result
t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
