import sys

# Input: List of books, each represented by a pair of integers (thickness, height)
#         Maximum shelf width
n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    thickness, height = map(int, input().split())
    for w in range(m + 1):
        dp[i][w] = min(dp[i-1][w], dp[i-1].get(w-thickness, float('inf')) + height)

print(dp[-1][-1])
