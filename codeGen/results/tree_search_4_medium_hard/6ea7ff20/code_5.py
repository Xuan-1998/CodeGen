def mergeable(p):
    n = len(p) // 2
    dp = [[False] * (len(p) + 1) for _ in range(n + 1)]
    
    # Initialize the base case
    dp[0][0] = True
    
    max_length = 0
    
    for i in range(1, n + 1):
        for j in range(len(p) + 1):
            if p[j - 1] < p[i - 1]:
                dp[i][j] = dp[i - 1][j]
            elif p[j - 1] > p[i - 1]:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        if not dp[i][len(p)]:
            return "NO"
    
    for i in range(n + 1):
        for j in range(len(p) + 1):
            if dp[i][j]:
                max_length = i
                break
    
    if max_length == n:
        return "YES"
    else:
        return "NO"

# Read input from stdin and write output to stdout
import sys
n = int(sys.stdin.readline().strip())
p = list(map(int, sys.stdin.readline().strip().split()))
print(mergeable(p))
