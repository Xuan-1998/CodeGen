import sys
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

dp = [[0] * (m + 1) for _ in range(n + 1)]
dq = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

max_similarity = 0
for i in range(n + 1):
    for j in range(m + 1):
        length_lcs = dp[i][j]
        if i > 0 and j > 0:
            max_similarity = max(max_similarity, 4 * length_lcs - (i + j))

print(max_similarity)
