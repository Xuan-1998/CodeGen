import sys

# Read input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for _ in range(m):
    l, r = map(int, input().split())
    queries.append((l-1, r))

# Dynamic programming to find the longest non-decreasing subsequence
dp = [False]*n
dp[0] = True
for i in range(1, n):
    dp[i] = any(dp[j] and arr[j] <= arr[i] for j in range(i))
max_length = max((i for i in range(n) if dp[i]), default=-1)

# Solve queries
for l, r in queries:
    if r-l+1 == max_length:
        print("Yes")
    else:
        print("No")
