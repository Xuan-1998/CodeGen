import sys

# Define a 2D array to store the minimum portal moves to reach each room.
dp = [0] * (10**3 + 1)

def solve(n):
    for i in range(1, n+1):
        # If p_{i-1} is odd and ceiling has an odd number of crosses
        if (p := dp[i-1]) % 2 == 1:
            dp[i] = min(dp[i-1], dp[p] + 1)
        else:
            dp[i] = dp[i-1]
    return dp[n+1]

n = int(input())
p = list(map(int, input().split()))
print(solve(n))
