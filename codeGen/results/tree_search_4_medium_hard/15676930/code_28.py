import sys
from collections import namedtuple

HareState = namedtuple('HareState', 'left_hungry right_hungry')
max_joy_values = [[0] * 2 for _ in range(2)]

def solve():
    n, a_values, b_values, c_values = [int(x) for x in input().split()]
    dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(n + 1)]
    max_joy_values[0][0] = max_joy_values[0][1] = 0

    for i in range(1, n + 1):
        if a_values[i - 1]:
            dp[i][0][0] = max(dp[i - 1][1][1], dp[i - 1][0][0]) + a_values[i - 1]
        else:
            dp[i][0][0] = max_joy_values[1][0]

        if b_values[i - 1]:
            dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][1][1]) + b_values[i - 1]
        else:
            dp[i][0][1] = max_joy_values[0][1]

        if c_values[i - 1]:
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][0][1]) + c_values[i - 1]
        else:
            dp[i][1][0] = max_joy_values[1][1]

    return dp[n][0][0]

print(solve())
