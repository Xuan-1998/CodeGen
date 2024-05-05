import sys

def read_ints():
    return map(int, raw_input().split())

n, m = read_ints()
a = raw_input().strip()
b = raw_input().strip()

dp = [[0] * (m+1) for _ in range(n+1)]
max_lcs_length = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            max_lcs_length = max(max_lcs_length, dp[i][j])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

max_similarity_score = 4 * max_lcs_length - (n + m)

print(max_similarity_score)
