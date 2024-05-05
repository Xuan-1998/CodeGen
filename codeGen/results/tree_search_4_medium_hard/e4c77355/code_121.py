===BEGIN SOLUTION===
from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

dp = [1] * n  # Initialize dp with all ones (subsequences of length 1)

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))  # Return the maximum value in the dp table
===END SOLUTION===
