from sys import stdin

def solve():
    initial_speed, final_speed, time, max_change = map(int, stdin.readline().split())
    dp = [[0] * (time + 1) for _ in range(101)]

    # Base case: initial speed
    for j in range(time + 1):
        dp[initial_speed][j] = j

    # Fill up the dp array
    for i in range(initial_speed + 1, final_speed):
        for j in range(time + 1):
            if j == 0:
                continue
            if abs(i - initial_speed) <= max_change and dp[initial_speed][j - 1] > 0:
                dp[i][j] = dp[initial_speed][j - 1] + j
            elif abs(i - final_speed) <= max_change and dp[final_speed][j - 1] > 0:
                dp[i][j] = dp[final_speed][j - 1] + j

    # Return the maximum length of the path segment that ends at the final speed
    return dp[final_speed][-1]

print(solve())
