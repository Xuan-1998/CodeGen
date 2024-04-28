def max_path_length():
    initial_speed, final_speed = map(int, input().split())
    time, max_diff = map(int, input().split())

    dp = [[0] * (max_diff + 1) for _ in range(time + 1)]

    for t in range(1, time + 1):
        for diff in range(max_diff + 1):
            if t == 1:
                dp[t][diff] = 1
            else:
                if -diff <= initial_speed - final_speed / (t + 1) <= diff:
                    dp[t][diff] = dp[t-1][diff] + 1
                else:
                    dp[t][diff] = max(dp[t-1][diff], dp[max(0, t-2)][min(diff, max_diff)])

    return dp[time][max_diff]

print(max_path_length())
