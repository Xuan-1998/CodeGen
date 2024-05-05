def max_or(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Calculate prefix sums and counts of 1's
    prefix_sum = [0]
    ones_count = [0]
    for i in range(1, n + 1):
        if s[i - 1] == '1':
            ones_count.append(ones_count[-1] + 1)
        else:
            ones_count.append(ones_count[-1])
        prefix_sum.append(prefix_sum[-1] + int(s[i - 1]))
    
    # Fill up the DP table
    for i in range(n, -1, -1):
        for j in range(i, -1, -1):
            if s[j] == '1':
                dp[i][j] = max(dp[i][j], prefix_sum[n] - prefix_sum[j] + ones_count[i])
            else:
                dp[i][j] = max(dp[i][j], prefix_sum[j])
    
    # Find the maximum OR
    max_or = 0
    for i in range(n):
        for j in range(i, n):
            max_or = max(max_or, dp[i + 1][j + 1] - ones_count[i] + ones_count[n - 1] - 2 ** (i + 1))
    
    return bin(max_or)[2:].zfill(n)

# Test the function
n = int(input())
s = input()
print(max_or(s))
