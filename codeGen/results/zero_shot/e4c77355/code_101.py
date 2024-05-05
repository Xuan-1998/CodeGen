import sys

n = int(input())  # Read the number of elements in the array
arr = list(map(int, input().split()))  # Read the array

dp = [1] * n  # Initialize the dp table with all elements set to 1

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))  # Print the maximum value in the dp table
