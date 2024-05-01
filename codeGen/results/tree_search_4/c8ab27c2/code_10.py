def shortest_common_subsequence_length(s1, s2):
    m, n = len(s1), len(s2)
    
    # Initialize DP table and memoization hash map
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    memo = {}
    
    # Fill the DP table and memoization hash map
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
            
            # Memoize intermediate results
            memo[(i, j)] = dp[i][j]
    
    # Find the minimum length of the shortest uncommon subsequence
    min_length = float('inf')
    for i in range(1, m + 1):
        if s1[i - 1] != s2[0]:
            min_length = min(min_length, memo.get((i, 0), dp[i][0]) + 1)
    
    # Return the minimum length or -1 if no such subsequence is possible
    return -1 if dp[m][n] == m + n else min_length

# Receive input from stdin and print output to stdout
s1 = input().strip()
s2 = input().strip()
print(shortest_common_subsequence_length(s1, s2))
