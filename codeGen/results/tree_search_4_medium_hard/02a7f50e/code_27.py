import sys

n = int(input())  # read n from stdin

dp = [0] * (n + 1)  # initialize dp table with zeros
dp[0] = 1  # base case: only one beacon can be added to the right of the first beacon

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if b[j] > b[i]:
            dp[i] = 1 + min(dp[j])  # calculate dp[i]

print(min(dp))  # print the minimum number of beacons that can be destroyed
