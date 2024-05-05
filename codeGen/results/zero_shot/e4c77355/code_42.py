# Step 1: Read the input array from standard input
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# Step 2: Initialize a dynamic programming table with size equal to the length of the input array
dp = [1]*n

# Step 3: Iterate over the input array and for each element, find the longest increasing subsequence ending at that element
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

# Step 4: The length of the longest increasing subsequence is the maximum value in the dynamic programming table
print(max(dp))
