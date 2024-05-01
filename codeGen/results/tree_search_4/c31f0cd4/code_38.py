import sys

# Read input
N = int(input())
a = list(map(int, input().split()))

# Sort array in ascending order
a.sort()

total_sum = sum(a)

# Initialize dynamic programming table
dp = [[0] * (total_sum + 1) for _ in range(N+1)]

for i in range(1, N+1):
    for k in range(total_sum, -1, -1):
        if k <= a[i-1]:
            dp[i][k] += dp[i-1][k-a[i-1]]

unique_sums = set()
for sum in range(1, total_sum + 1):
    if sum not in unique_sums:
        print(sum, end=' ')
