def max_common_substrings():
    str1, str2 = input().split()
    N = len(str1)
    
    # Create a 2D table to store counts of common non-overlapping substrings
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Initialize the DP table with base cases
    for i in range(N):
        for j in range(N):
            if str1[i] == str2[j]:
                dp[i][j] = 1
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    
    # Find the maximum number of common non-overlapping substrings
    max_count = 0
    for i in range(N):
        for j in range(N):
            if str1[i] == str2[j]:
                max_count += dp[i][j]
    
    print(max_count)

max_common_substrings()
