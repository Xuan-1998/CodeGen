import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1)
ones = {0}
for i in range(1, n + 1):
    if str(bin(i))[2:].count('11') == 0:  # check if consecutive ones are present
        dp[i] = len(ones)  # update DP array with the current set size
        ones.update(range(i))  # add new numbers to the set
    else:
        dp[i] = dp[i - 1]
print(dp[n])
