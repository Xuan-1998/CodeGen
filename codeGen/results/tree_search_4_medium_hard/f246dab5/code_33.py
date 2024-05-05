import sys

def solve():
    n = int(input())  # Read the number of trips from input
    dp = [float('inf')] * (10**9 + 5)  # Initialize dp array with infinite values
    dp[0] = 0  # The minimum cost to reach time 0 is 0

    for _ in range(n):
        t = int(input())  # Read the timestamp of the current trip from input
        if t == 1:
            print(20)  # Print the fare charged after this trip (1-day ticket)
        else:
            dp[t] = min(dp[max(0, t - 1440)] + 120, dp[max(0, t - 90)] + 50)  # Update dp value
            print(dp[t])  # Print the fare charged after this trip

solve()
