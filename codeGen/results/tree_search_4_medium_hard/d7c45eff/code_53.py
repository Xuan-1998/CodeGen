import sys

def get_smallest_string(n, k):
    s = input().strip()
    dp = [[[] for _ in range(k+1)] for _ in range(n+1)]

    # Base case: If k is 0, return an empty string as there are no characters left to consider.
    dp[0][0] = ''

    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            if j < i:
                # Consider deleting the last character of s.
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1][-1] + dp[i-1][j-1]) 
            else:
                # Consider duplicating the original string. 
                dp[i][k] = s[:i-1] + dp[i-1][k]

    return dp[n][k]


n, k = map(int, input().split())
print(get_smallest_string(n, k))
