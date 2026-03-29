===BEGIN CODE===
import sys
from math import ceil, floor

def solve():
    n, t = map(int, input().split())
    num = [int(x) for x in str(input()).split('.')[1]]

    # Initialize the dp array with zeros and set dp[0] to 1 (assuming maximum grade for a single-digit decimal is 1)
    dp = [0] * (n + 1); dp[0] = 1

    for i in range(1, n + 1):
        average = (num[i - 1] * 10 + num[i]) / 2
        ceil_avg, floor_avg = int(ceil(average)), int(floor(average))
        
        # Update dp[i] as the maximum of:
        # a) The previous maximum: dp[i - 1]
        # b) And the maximum grade that can be obtained by rounding the current digit, which is either ceil or floor of the average
        if i < t + 1:
            dp[i] = max(dp[i - 1], min(ceil_avg, floor_avg))
        else:
            dp[i] = dp[i - 1]

    # Return dp[n] as the maximum possible grade that can be obtained for the given decimal fraction within time limit t
    return dp[n]

print(solve())
===END CODE===
