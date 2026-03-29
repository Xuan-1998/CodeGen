import sys
n = int(input())  # Get the size of the array
arr = list(map(int, input().split()))  # Read the array

dp = [0] * n  # Initialize a dynamic programming table with zeros
dp[0] = arr[0]  # The maximum reachable position at index 0 is the value at that index

for i in range(1, n):
    dp[i] = max(min(i + arr[i], n - 1), dp[i-1]) if i > 0 else i

print(dp[-1] == n - 1)  # Check if we can reach the last index
