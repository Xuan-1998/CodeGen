import sys

N = int(input())  # read N from input
nums = list(map(int, input().split()))  # read N numbers from input
total = sum(nums)  # calculate the total sum of the set

dp = {}  # initialize dp as an empty dictionary
for i in range(1, N+1):  # iterate over each element in the set
    for t in range(total + 1):  # iterate over each possible sum
        dp[i][t] = dp.get(i-1, {}).get(t, 0) + (1 if nums[i-1] <= t else 0)

# print the distinct sums
for t in sorted(dp[N].keys()):
    print(t, end=' ')
