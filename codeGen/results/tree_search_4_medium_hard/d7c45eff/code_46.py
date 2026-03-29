def find_smallest_string():
    n, k = map(int, input().split())
    s = input()

    dp = [[[False for _ in range(k+1)] for _ in range(n+1)] for _ in range(2)]

    for i in range(n+1):
        dp[0][i][0] = (i == 0)  # base case: empty string is always lexicographically smaller
        if i > 0:
            dp[0][i][1] = dp[0][i-1][1]

    for j in range(k+1):
        for i in range(n+1):
            if i == n and j < k:
                dp[1][n][j] = (dp[1][n-1][j-1][0] or dp[1][n-1][j-1][1])  # duplicate the last character
            elif i > 0 and j > 0:
                dp[1][i][j] = (s[i-1] < s[i-2] and dp[1][i-1][j-1][0] or dp[1][i-1][j-1][1])  # delete the last character
            else:
                dp[1][i][j] = (i == 0)  # base case: empty string is always lexicographically smaller

    ans = []
    for j in range(k, -1, -1):
        if dp[1][n][j]:
            ans.append(s[:k-j])
            break
    return ''.join(ans)

print(find_smallest_string())
