import sys

def solve():
    # Read input
    initial_speed, final_speed = map(int, input().split())
    time, allowed_change_in_speed = map(int, input().split())

    # Initialize DP table
    dp = [[0] * (allowed_change_in_speed + 1) for _ in range(time + 1)]

    # Fill the DP table
    for i in range(1, time + 1):
        for diff in range(1, allowed_change_in_speed + 1):
            if i == 1:
                dp[i][diff] = min(initial_speed, final_speed) * i
            else:
                dp[i][diff] = max(dp[i-1][diff-1], dp[i-1][diff+1]) + min(initial_speed, final_speed)

    # Find the maximum possible length of path segment with a difference in speed equal to 0 (i.e., constant speed)
    max_length = max(dp[-1])

    print(max_length)

if __name__ == "__main__":
    solve()
