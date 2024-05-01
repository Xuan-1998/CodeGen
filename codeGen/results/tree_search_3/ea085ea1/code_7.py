===BEGIN CODE===
def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # Create a hash map to store the maximum number of common non-overlapping substrings for each prefix of str1
    prefix_map = {}
    for i in range(N):
        if str1[:i+1] not in prefix_map:
            prefix_map[str1[:i+1]] = 0
        for j in range(i, N):
            if str1[i:j+1] == str2[j-i:j+1]:
                dp[i][j] = max(dp[i][j], 1 + (prefix_map.get(str1[:i], 0) or 0))
                prefix_map[str1[:i+1]] = dp[i][j]

    return max(max(row) for row in dp)
