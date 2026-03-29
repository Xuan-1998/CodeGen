import sys

N = int(input())  # Read the length of the array
A = list(map(int, input().split()))  # Read the array elements

dp = {0: 0}  # Initialize the DP dictionary with dp[0] = 0

for i in range(1, N):
    min_ops = sys.maxsize
    for j in range(i):
        min_ops = min(min_ops, dp[j] + abs(A[i] - A[j]))
    dp[i] = min_ops

print(dp[N-1])  # Print the minimum number of operations required to make the entire array strictly increasing
