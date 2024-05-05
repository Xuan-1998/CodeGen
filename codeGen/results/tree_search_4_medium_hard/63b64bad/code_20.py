import sys
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

dp = defaultdict(lambda: {k: {} for k in range(1, n+2)})  # Initialize dynamic programming table

def simulate_program(x, y):
    if x > n:
        return -1
    elif dp[x][x][y]:
        return dp[x][x][y]
    else:
        new_x = x + a[x]
        new_y = y + a[x]
        if (new_x, new_y) in dp[new_x][new_x]:
            dp[new_x][new_x][new_y] = -1
        else:
            result = simulate_program(new_x, new_y)
            if result == -1:
                return -1
            elif result > 0:
                dp[x][x][y] = result
        return new_y

for i in range(2, n+1):
    print(simulate_program(1, 0))
