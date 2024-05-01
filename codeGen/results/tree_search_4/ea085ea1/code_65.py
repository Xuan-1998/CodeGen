def find_max_common_substrings(str1, str2):
    N = len(str1)
    
    # Initialize prefix_dp array
    prefix_dp = [0] * (N + 1)
    for i in range(1, N + 1):
        if str1[i - 1] == str2[0]:
            prefix_dp[i] = prefix_dp[i - 1] + 1
        else:
            prefix_dp[i] = prefix_dp[i - 1]
    
    # Initialize dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Fill up the dp table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Return the maximum value in the dp table
    return max(max(row) for row in dp)

str1 = input()
str2 = input()

print(find_max_common_substrings(str1, str2))
