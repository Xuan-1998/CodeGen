def min_changes(s, k):
    n = len(s)
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    
    # Base case: no changes needed if the substring is already correct
    for i in range(k, -1, -1):
        dp[i][0] = 0
    
    # Fill up the dp table using dynamic programming and memoization
    for i in range(1, n + 1):
        for j in range(min(i, k), -1, -1):
            if s[i-1] == 'R':
                changes = dp[max(0, i-k)][j]
            elif s[i-1] == 'G':
                changes = dp[max(0, i-k)][min(j+1, k)] + 1
            else:
                changes = dp[max(0, i-k)][j] + 1
            
            if j > 0 and (s[i-1] != s[(i-1)-k]):
                changes += 1
            
            dp[i][j] = min(changes, dp[i-1][j])
    
    # The minimum number of changes needed is stored in the last cell
    return dp[n][k]

# Read input from stdin and process each query
while True:
    try:
        n, k = map(int, input().split())
        s = input()
        
        print(min_changes(s, k))
    except EOFError:
        break
